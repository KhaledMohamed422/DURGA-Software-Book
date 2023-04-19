from . import views
from django.urls import path

# from django.conf.urls import url
urlpatterns = [
    path('post_list', views.post_list_view, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail_view, name='post_detail'),
    path("sendmail",views.sendMail, name="sendmail"),
    path('<int:id>/share/', views.mail_send_view ,name='mail_send_view'),
    path('tag/<slug:tag_slug>/', views.post_list_view, name='post_list_by_tag_name'),

 
]
