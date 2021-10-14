from django.contrib.auth import get_user_model, authenticate, login, logout

from django.shortcuts import redirect, render
# from .forms import LoginForm, RegisterForm, User
# Create your views here.

from .forms import *

# ---------------------------------------------------------------------REGISTER VIEW--------------------------------------------------


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")

        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
    # if user fill the valid data : then 'LOGIN'
        if user != None:
            login(request, user)
            return redirect("/dashboard")

    # if user fill invalid data ( username or password) in the form
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")

            # another way for the same done above is given below:

            request.session['register_error'] = 1  # 1 == True

    return render(request, "forms.html", {"form": form})


# ---------------------------------------------------------------------LOGIN VIEW--------------------------------------------------

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        check_username = User.objects.get(username=username)
    # if user fill the valid data : then 'LOGIN'

        if user != None:
            # user is vlaid and active --> is_active
            # request.user == user
            login(request, user)
            return redirect("/create")

    # if user fill invalid data ( username or password) in the form
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")

            # another way for the same done above is given below:

            request.session['invalid_user'] = 1  # 1 == True

    return render(request, "forms.html", {"form": form})

# ---------------------------------------------------------------------LOGOUT VIEW--------------------------------------------------


def logout_view(request):
    logout(request)
    # request.user == Anonymous user
    return redirect("/login")
