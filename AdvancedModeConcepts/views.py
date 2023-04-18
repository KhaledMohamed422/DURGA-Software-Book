from django.shortcuts import render
from .models import Employee, ProxyEmployee1, ProxyEmployee2


def display_view(request):
    # employees=Employee.objects.all()
    # employees=ProxyEmployee.objects.all()
    employees = ProxyEmployee2.objects.all()
    my_dict = {'employees': employees}
    return render(request, 'index.html', my_dict)
