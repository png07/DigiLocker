from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Document

class UserSignupForm(UserCreationForm):
    username = forms.CharField(label="Username", help_text="")
    password1 = forms.CharField(label="Password", help_text="", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", help_text="", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file_name', 'encrypted_file']  # Ensure these fields are included

