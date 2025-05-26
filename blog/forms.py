from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Blog



class AuthorSignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password',}))
    password2 = forms.CharField(label="Repeat your password", widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Repeat your password',}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control form-control-lg'}) ,
            'first_name': forms.TextInput(attrs={'placeholder': 'Firstname', 'class': 'form-control form-control-lg'}) ,
            'last_name': forms.TextInput(attrs={'placeholder': 'Lastname', 'class': 'form-control form-control-lg'}) ,
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email',}),
        }


class AuthorLoginForm(AuthenticationForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Password'
        })
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Username',
        })
    )


class AddBlogPostForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['title', 'sub_title','description']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title..', 'class': 'form-control'}) ,
            'sub_title': forms.TextInput(attrs={'placeholder': 'Sub Title..', 'class': 'form-control'}) ,
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}) ,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_title'].required = False