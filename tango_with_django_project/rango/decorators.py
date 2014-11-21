from functools import wraps
from django.http import HttpResponseRedirect

def login_required(func):
    def _wrap(request, *args, **kwargs):       
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/rango/login/')
        return func(request, *args, **kwargs)
    return _wrap