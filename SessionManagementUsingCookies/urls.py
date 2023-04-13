from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name='index'),
    path('check_cookie', views.check_cookie, name='check_cookie'),
    path('count_view', views.count_view, name='count_view'),
    path('name_view', views.name_view, name='name_view'),
    path('age_view', views.age_view, name='age_view'),
    path('gf_view', views.gf_view, name='gf_view'),
    path('results_view', views.results_view, name='results_view'),
]
