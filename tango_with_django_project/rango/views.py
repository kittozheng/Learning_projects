from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rango.models import Category, Page
from rango.forms import UserForm, UserProfileForm,CategoryForm, PageForm
from rango.decorators import login_required
from rango.bing_search import run_query

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
    context.update(dict(result_list=None, query=None))

    if request.method == "POST":
        query = request.POST['query'].strip()
        if query:
            query = query.strip()
            result_list = run_query(query)
            context.update(result_list=result_list,query=query)
    try:
        category = Category.objects.get(name=category_name_slug)
        pages = Page.objects.filter(category=category).order_by('-views')
        admin = Page.objects.get(category=Category.objects.get(name='Admin'))
        
        context.update(dict(category_name=category.name,
                            category=category,
                            pages=pages,
                            admin=admin,
                            profile=request.user,))
        context.update(csrf(request))
    except Category.DoesNotExist:
        pass

    if not context['query']:
        context.update(dict())

    print "*"*10
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
                
@login_required
def track_url(request):
    url = '/rango/'
    if request.method == 'GET':
        page_id = request.GET.get('page_id', None)
        try:
            page = Page.objects.get(id=page_id)
            page.views = page.views + 1
            page.save()
            url = page.url
        except:
            pass
    return redirect(url)

@login_required
def search(request):
    if request.method == "POST":
        query = request.POST.get('query', None)
        context = dict()
        if query:
            query = query.strip()
            result_list = run_query(query)
            context.update(dict(result_list=result_list))
        return render_to_response('rango/search.html', context)

@login_required
def like_category(request):
    if request.method == "GET":
        profile = request.user
        cat_id = int(request.GET.get('category_id', None))
        likes = 0
        if cat_id:
            try:
                cat = Category.objects.get(id=cat_id)
                cat.likes = cat.likes + 1
                cat.save()
                likes = cat.likes
            except:
                pass
        return HttpResponse(likes)

def get_category_list(max_results=0, start_with=''):
    cat_list = []
    if start_with:
        cat_list = Category.objects.filter(name__istartwith=start_with)
    if max_results > 0:
        if Count(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list

@login_required
def suggest_category(request):
    start_with = ''
    if request.method == 'GET':
        start_with = request.GET.get('suggestion', None)
    cat_list = get_category_list(8, start_with)
    context = dict(cat_list=cat_list)

    print cat_list
    return render_to_response('rango/category_list.html', context)

