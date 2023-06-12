from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, SignupForm
def signin(request):
    msg = None
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating"
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {"form": form, "msg": msg})

# signin
def signup(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignupForm(data=request.POST)

        if form.is_valid():
            form.save()
            msg = "User created - Please <a href='/login'>Login</a>"
            success = True
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/signin')
        else:
            msg = "Form is not valid"
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form, "msg": msg, "success": success})

# signout
def signout(request):
    logout(request)
    return redirect('/')