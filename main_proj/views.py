from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
class Home(TemplateView):
    template_name='main_proj/index.html'

class About(TemplateView):
    template_name='main_proj/about.html'

class Services(TemplateView):
    template_name='main_proj/services.html'    

class Courses(TemplateView):
    template_name='main_proj/courses.html'    

class Pricing(TemplateView):
    template_name='main_proj/pricing.html'      

class Contact(TemplateView):
    template_name='main_proj/contact.html'    

class Registration(TemplateView):
    template_name='main_proj/registration.html'      