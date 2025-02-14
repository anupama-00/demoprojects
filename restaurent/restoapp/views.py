from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView

from restoapp.models import Menuitem,Menu


# Create your views here.
class Home(ListView):
    model = Menu
    template_name = 'home.html'
    context_object_name = 'm'

class Menuitems(CreateView):
    model = Menuitem
    template_name = 'menuitem.html'
    fields = ['name','price','menu','is_vegetarian']
    success_url = reverse_lazy('home')

# class Menudetails(DetailView):
#     model = Menu
#     template_name = 'menudetails.html'
#     context_object_name = 'details'

def menudetails(request,i):
    m=Menu.objects.get(id=i)
    context={'menu':m}
    return render(request,'menudetails.html',context)

class Menuupdate(UpdateView):
    model = Menuitem
    template_name = 'update.html'
    fields = ['price']
    success_url = reverse_lazy('home')




