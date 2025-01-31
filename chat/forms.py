import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:  # type: ignore
            raise forms.ValidationError(
                "Username must be at least 3 characters.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:  # type: ignore
            raise forms.ValidationError(
                "Password must be at least 8 characters long.")
        if not re.search(r"[A-Za-z]", password):  # type: ignore
            raise forms.ValidationError(
                "Password must contain at least one letter.")
        if not re.search(r"\d", password):  # type: ignore
            raise forms.ValidationError(
                "Password must contain at least one number.")
        if not re.search(r"[@$!%*?&]", password):  # type: ignore
            raise forms.ValidationError(
                "Password must contain at least one symbol (@, $, !, %, etc.).")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username does not exist.")
        return username
