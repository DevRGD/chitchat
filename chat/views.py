from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def home(request):
    return render(request, "home.html")


def chat(request):
    return render(request, "chat.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, "signup.html", {'form': form})

    else:
        form = SignUpForm()
        return render(request, "signup.html", {'form': form})


def password_reset(request):
    return render(request, 'password_reset.html')


def password_reset_mail(request):
    return render(request, 'password_reset_mail.html')
