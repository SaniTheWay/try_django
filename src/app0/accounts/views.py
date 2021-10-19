from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from showcase.models import Showcase
# from .forms import LoginForm, RegisterForm, User
# Create your views here.
from .forms import *

User = get_user_model()


# ---------------------------------------------------------------------REGISTER VIEW--------------------------------------------------


def register_view(request):
    if not request.user.is_authenticated:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            organization = form.cleaned_data.get('organization')
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")

            try:
                user = User.objects.create_user(
                    username, email, password, first_name, last_name)
            except:
                user = None
        # if user fill the valid data : then 'LOGIN'
            if user != None:
                login(request, user)
                # messages.success(request, "Registration successful.")
                return redirect("/dashboard")

        # if user fill invalid data ( username or password) in the form
            else:
                # attempt = request.session.get("attempt") or 0
                # request.session['attempt'] = attempt + 1
                # return redirect("/invalid-password")

                # another way for the same done above is given below:

                request.session['register_error'] = 1  # 1 == True

        return render(request, "accounts/forms.html", {"form": form})
    else:
        return redirect("/")

# ---------------------------------------------------------------------LOGIN VIEW--------------------------------------------------


def login_view(request):
    if not request.user.is_authenticated:
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
                return redirect("/dashboard")

        # if user fill invalid data ( username or password) in the form
            else:
                # attempt = request.session.get("attempt") or 0
                # request.session['attempt'] = attempt + 1
                # return redirect("/invalid-password")

                # another way for the same done above is given below:

                request.session['invalid_user'] = 1  # 1 == True

        return render(request, "accounts/forms.html", {"form": form})

    else:
        return redirect("/")

# ---------------------------------------------------------------------LOGOUT VIEW--------------------------------------------------


def logout_view(request):
    logout(request)
    # request.user == Anonymous user
    return redirect("/login")


@login_required(redirect_field_name='projectyverse')
def profile_view(request, *args, **kwargs):
    user = User.objects.get(username=request.user)
    # username = request.user,
    profile_context = {

        "profile": user,
        # "first_name": User.objects.get(username='sani1')
    }
    return render(request, "accounts/profile.html", profile_context)


@login_required
def profile_project_view(request, *args, **kwargs):
    qs = Showcase.objects.all()
    context = {
        "object_list": qs,

    }
    return render(request, "accounts/list.html", context)
