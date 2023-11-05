from django.shortcuts import render
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import Number
from django.views.generic import CreateView, ListView


# Create your views here.
class NumberForm(ModelForm):
    class Meta:
        model = Number
        fields = ('number',)
        
class ListNumber(ListView):
    model = Number
    template_name = 'numbers.html'
    context_object_name = 'numbers'


class CreateNumber(CreateView):
    model = Number
    form_class = NumberForm
    template_name = 'create_number.html'
    success_url = reverse_lazy('list')
