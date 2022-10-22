from django.contrib import admin
from django.urls import path, include
from helsings_school import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('staff', views.staff, name='staff'),
    path('alumni', views.alumni, name='alumni'),
    path('table', views.table, name='table'),
]
