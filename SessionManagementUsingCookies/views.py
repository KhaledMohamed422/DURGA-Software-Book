from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm 
import datetime 
# Create your views here.


# Test for (cookies are working on this website or no )
def index(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1>index Page</h1>')


def check_cookie(request):
    if request.session.test_cookie_worked():
        return HttpResponse('<h1>cookies are working properly</h1>')
    # request.session.delete_test_cookie()
    return HttpResponse('<h1>Checking Page</h1>')


# Application-1 Session Management by using Cookies (PageCount Application)
def count_view(request):
    if 'count' in request.COOKIES:
        newcount = int(request.COOKIES['count']) + 1
    else:
        newcount = 1
    response = render(request, 'SessionManagementUsingCookies/count.html', {'count': newcount})
    response.set_cookie('count', newcount)
    return response

# Application-2 Session Management by using Cookies 
def name_view(request): 
    return render(request,'SessionManagementUsingCookies/name.html') 

def age_view(request): 
    name=request.GET['name'] 
    response=render(request,'SessionManagementUsingCookies/age.html',{'name':name}) 
    response.set_cookie('name',name) 
    return response 

def gf_view(request): 
    age=request.GET['age'] 
    name=request.COOKIES['name'] 
    response=render(request,'SessionManagementUsingCookies/gf.html',{'name':name}) 
    response.set_cookie('age',age) 
    return response 
 
def results_view(request): 
    name=request.COOKIES['name'] 
    age=request.COOKIES['age'] 
    gfname=request.GET['gfname'] 
    response=render(request,'SessionManagementUsingCookies/results.html',{'name':name,'age':age,' gfname':gfname}) 
    response.set_cookie('gfname',gfname) 
    return response