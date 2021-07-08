from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render

from cats.models import Cat , Breed


# Create your views here.
class CatList(LoginRequiredMixin , View):
    def get(self , request):
        b = Breed.objects.all().count()
        c = Cat.objects.all()
        ctx = {'breed_count': b , 'cat_list': c}
        return render(request, 'cats/cat_list.html', ctx)

class BreedView(LoginRequiredMixin , View):
    def get(self , request):
        bl = Breed.objects.all()
        ctx = {'breed_list': bl}
        return render(request, 'cats/breed_list.html', ctx)

class CatCreate(LoginRequiredMixin , CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class CatUpdate(LoginRequiredMixin , UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class CatDelete(LoginRequiredMixin , DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class BreedCreate(LoginRequiredMixin , CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedUpdate(LoginRequiredMixin , UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedDelete(LoginRequiredMixin , DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')
