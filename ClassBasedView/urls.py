from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('khaled/', ProductListView.printKhaled, name='printKhaled'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='ProductCreateView'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='ProductUpdateView'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='ProductDeleteView'),
    
]
