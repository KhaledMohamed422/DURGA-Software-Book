from . import views
from django.urls import path

urlpatterns = [
    path('page_count_view', views.page_count_view, name='page_count_view'),
    path('name_view', views.name_view, name='name_view'),
    path('age_view', views.age_view, name='age_view'),
    path('gf_view', views.gf_view, name='gf_view'),
    path('results_view', views.results_view, name='results_view'),
    path('add_item_view', views.add_item_view, name='add_item_view'),
    path('display_items_view', views.display_items_view, name='display_items_view'),

]
