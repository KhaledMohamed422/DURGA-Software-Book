from .forms import *
from django.shortcuts import render

# Create your views here.

# Application-1 Session Management by using Session API (PageCount Application)
"""
    The purpose of this view is to display a count of how many times the user has visited the page. To do this, it uses session management to keep track of the count.
"""


def page_count_view(request):
    # count = request.session.get('count', 0)
    # newcount = count+1
    # request.session['count'] = newcount
    # print(request.session.get_expiry_age())
    # print(request.session.get_expiry_date())
    request.session['name'] = 'khaled'
    request.session['age'] = 20

    newcount = request.session['name'] + str(request.session['age'])
    return render(request, 'SessionManagementBysingSessionAPI/pagecount.html', {'count': newcount})

# Application-2 Session Management by using Session API (Profile Application)


def name_view(request):

    form = NameForm()
    return render(request, 'SessionManagementBysingSessionAPI/name.html', {'form': form})


def age_view(request):

    name = request.GET['name']
    request.session['name'] = name
    form = AgeForm()
    return render(request, 'SessionManagementBysingSessionAPI/age.html', {'form': form})


def gf_view(request):

    age = request.GET['age']
    request.session['age'] = age
    form = GFForm()
    return render(request, 'SessionManagementBysingSessionAPI/gf.html', {'form': form})


def results_view(request):

    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, 'SessionManagementBysingSessionAPI/results.html')

# Application-3 Session Management by using Session API (Shopping Cart Application)
def add_item_view(request):

    form = AddItemForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
    return render(request, 'SessionManagementBysingSessionAPI/additem.html', {'form': form})


def display_items_view(request):
    return render(request, 'SessionManagementBysingSessionAPI/displayitems.html')
