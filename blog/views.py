from django.shortcuts import render, redirect
from .forms import AuthorSignUpForm, AuthorLoginForm, AddBlogPostForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, logout, login as auth_login, update_session_auth_hash
from .models import Blog


def home_page(request):
    posts = Blog.objects.all()
    values = {
        "posts": posts
    }
    return render(request, "index.html", values)

def about(request):
    return render(request, "about.html")

def contact_us(request):
    return render(request, "contact_us.html")

def author_signup_form(request):
    if request.method == 'POST':
        fm = AuthorSignUpForm(request.POST, label_suffix="")
        if fm.is_valid():
            messages.success(request, 'Registration has been successfully submitted!!')
            user = fm.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            return redirect('/')
    else:
        fm = AuthorSignUpForm(label_suffix="")
    return render(request, "author_signup_form.html", {"form":fm})


def login_form(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthorLoginForm(request=request, data=request.POST, label_suffix="")
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    auth_login(request, user)
                    return redirect('/')
        else:
            fm = AuthorLoginForm(label_suffix="")
        return render(request, "login_form.html", {"form":fm})
    else:
        return redirect('/')
    
def user_logout(request):
    logout(request)
    return redirect('/')


def dashboard(request):

    return render(request, "dashboard.html")

def add_post(request):
    if request.method == 'POST':
        post_data = AddBlogPostForm(request.POST)
        if post_data.is_valid():
            post_data.save()
            messages.success(request, 'Form has been successfully submitted!!')
            print(messages.get_level(request))
            return redirect('/dashboard')
    else:
        post_data = AddBlogPostForm()

    values = {
        "form": post_data
    }
    print(f'\n\n\n  {values = }  \n\n')
    return render(request, "add_post.html", values)

def show_post(request, id):
    post = Blog.objects.get(pk=id)
    values = {
        "post": post
    }
    return render(request, "post.html", values)
