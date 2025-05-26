"""
URL configuration for mini_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about, name="about"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('signup/', views.author_signup_form, name="signup"),
    path('login/', views.login_form, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_post/', views.add_post, name="add_post"),
    path('add_post/<int:id>/', views.add_post, name="add_post"),
    path('post/<int:id>/', views.show_post, name="post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
]
