from django.urls import path
from . import views

urlpatterns = [
    path('welcome_view',views.welcome_view,name='welcome_view'),
    path('home_page_view',views.home_page_view,name='home_page_view'),
    
]
