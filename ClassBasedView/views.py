from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import *
from django.views.generic import CreateView


class ProductListView(ListView):

    # Way1 to declare queryset and template_name and context_object_name by attribute
    model = Product
    template_name = 'product_list.html'
    # context_object_name = 'product'

    # Way2 to declare queryset by attribute
    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     return queryset

    # NewMethon within Class

    def printKhaled(self):
        print("khaled")
        return HttpResponse('hello')


class ProductDetailView(DetailView):
    # Url to each a particuler object based on by default id
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'price')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = 'http://127.0.0.1:8000/ClassBasedView/'



