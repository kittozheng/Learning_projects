from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from rango.models import Category, Page
from rango.forms import UserForm, UserProfileForm,\
                        CategoryForm, PageForm
from rango.decorators import login_required

from datetime import datetime


# Create your views here.

def register(request):
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    context = dict(user_form=user_form, 
                   profile_form=profile_form,
                   registered=registered,)
    context.update(csrf(request))
    
    return render_to_response('rango/register.html',context)

def user_login(request):
    
    context = dict()   
    context.update(csrf(request))        
    
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/', context)
            else:
                return HttpResponse("Your rango account is disabled")
        else:
            print "Invalid login details:{0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render_to_response('rango/login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('rango/login/')

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text")

@login_required
def index(request): 
    context = dict(user=request.user)
    
    category_list = Category.objects.all()
    page_list = Page.objects.order_by('-views')[:5]
    context.update(dict(categories=category_list, pages=page_list,profile=request.user))

    # cookie
    # visits = int(request.COOKIES.get('visits', '0'))
    # reset_last_visit_time = False
    # if 'last_visit' in request.COOKIES:
    #     last_visit = request.COOKIES['last_visit']
    #     last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
    #     if (datetime.now() - last_visit_time).seconds > 5:
    #         visits = visits + 1
    #         reset_last_visit_time = True
    # else:
    #     reset_last_visit_time = True
    
    # response = render_to_response('rango/index.html', context)
    # if reset_last_visit_time:
    #     response.set_cookie('last_visit', datetime.now())
    # response.set_cookie('visits', visits)    
    # visits = request.session.get('visits', 0)
    # reset_last_visit_time = False

    # return response
    visits = int(request.session.get('visits', 0))
    reset_last_visit_time = False
    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if(datetime.now() - last_visit_time).seconds > 5:
            visits = visits + 1
        reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    context.update(dict(visits=visits))
    
    request.session['visits'] = visits
    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now()) 

    response = render_to_response('rango/index.html',  context)
    return response

@login_required
def about(request):
    contact = "kittozhengszu@gmail.com"
    context = dict(user=request.user, contact=contact,profile=request.user,)
    return render_to_response('rango/index.html', context)

@login_required
def show_category(request):
    category_list = Category.objects.order_by('name')[:5].values('name')
    context = dict(categories=category_list, 
                                is_authenticated=request.user.is_authenticated,
                                profile=request.user,)
    context.update(csrf(request))
    return render_to_response("rango/show_category.html", context)

@login_required
def category(request, category_name_slug):
    context = dict()
    try:
        category = Category.objects.get(name=category_name_slug)
        pages = Page.objects.filter(category=category)
        admin = Page.objects.get(category=Category.objects.get(name='Admin'))
        
        context.update(dict(category_name=category.name,
                            category=category,
                            pages=pages,
                            admin=admin,
                            profile=request.user,))
        context.update(csrf(request))
    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context)

@login_required
def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return show_category(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    
    context = dict(form=form, profile=request.user,)
    context.update(csrf(request))
    return render_to_response('rango/add_category.html', context)

@login_required
def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(name = category_name_slug)
    except Category.DoesNotExist:
        cat = None
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context = dict(form=form,
                                profile=request.user, 
                                category=cat, 
                                category_name_url=category_name_slug,)
    context.update(csrf(request))
    
    return render_to_response('rango/add_page.html', context)
                
