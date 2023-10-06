from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import *

class CarsView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

class AboutCar(DetailView):
    model = Car
    template_name = 'about.html'
    context_object_name = 'car'

class CreateCar(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

class DeletePicture(DeleteView):    
    model = Car
    template_name = 'delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')