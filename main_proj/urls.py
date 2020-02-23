from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.Home.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    path('services', views.Services.as_view(), name='services'),
    path('courses', views.Courses.as_view(), name='courses'),
    path('pricing', views.Pricing.as_view(), name='pricing'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('registration', views.Registration.as_view(), name='registration'),
]
