from django.views.generic import ListView, TemplateView
from .models import Data 
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render



class DataListView(ListView):
	model = Data
	template_name = 'cases.html'
	

class HomePageView(TemplateView):
	template_name = 'index.html'