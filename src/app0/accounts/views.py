from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import request
from django.utils.http import is_safe_url, urlquote
from django.views.generic import CreateView, FormView
from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from showcase.models import Showcase
# from .forms import LoginForm, RegisterForm, User
# Create your views here.
from .forms import *

User = get_user_model()

# -------------CHANGING TO CLASS BASED VIEW----------------------------------


class RegisterView(CreateView):
    # define form class
    form_class = Registermodelform
    template_name = 'accounts/forms.html'
    success_url = "/login/"


# ---------------------------------------------------------------------REGISTER VIEW--------------------------------------------------


# def register_view(request):
#     if not request.user.is_authenticated:
#         form = Registermodelform(request.POST or None)
#         if form.is_valid():
#             email = form.cleaned_data.get("email")
#             # email = form.cleaned_data.get("email")
#             password = form.cleaned_data.get("password")
#             password_2 = form.cleaned_data.get("password_2")

#             try:
#                 user = User.objects.create_user(
#                     email, password)
#             except:
#                 user = None
#         # if user fill the valid data : then 'LOGIN'
#             if user != None:
#                 login(request, user)
#                 # messages.success(request, "Registration successful.")
#                 return redirect("/dashboard")

#         # if user fill invalid data ( username or password) in the form
#             else:
#                 # attempt = request.session.get("attempt") or 0
#                 # request.session['attempt'] = attempt + 1
#                 # return redirect("/invalid-password")

#                 # another way for the same done above is given below:

#                 request.session['register_error'] = 1  # 1 == True

#         return render(request, "accounts/forms.html", {"form": form})
#     else:
#         return redirect("/")

# ---------------------------END of REGISTER VIEW---------------------------------------------

# ---------------------------STARTING LOGINVIEW-----------------------------------------------

#  ------------------CLASS BASED LOGIN VIEW---------------------------------------------------

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/forms.html'
    success_url = '/'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=email, password=password)
        print(user)

        if user != None:
            login(request, user)
            # user is vlaid and active --> is_active
            # request.user == user
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return render(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


# ---------------------------------------------------------------------LOGIN VIEW--------------------------------------------------


# def login_view(request):
#     if not request.user.is_authenticated:
#         form = LoginForm(request.POST or None)
#         if form.is_valid():
#             email = form.cleaned_data.get("email")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=email, password=password)
#             # check_username = User.objects.get(email=email)
#         # if user fill the valid data : then 'LOGIN'

#             if user != None:
#                 # user is vlaid and active --> is_active
#                 # request.user == user
#                 login(request, user)
#                 return redirect("/dashboard")

#         # if user fill invalid data ( username or password) in the form
#             else:
#                 # attempt = request.session.get("attempt") or 0
#                 # request.session['attempt'] = attempt + 1
#                 # return redirect("/invalid-password")

#                 # another way for the same done above is given below:

#                 request.session['invalid_user'] = 1  # 1 == True

#         return render(request, "accounts/forms.html", {"form": form})

#     else:
#         return redirect("/")

# ---------------------------------------------------------------------LOGOUT VIEW--------------------------------------------------


def logout_view(request):
    logout(request)
    # request.user == Anonymous user
    return redirect("/login")


# @login_required(redirect_field_name='projectyverse')
# def profile_view(request, *args, **kwargs):
#     user = User.objects.get(email=request.user)
#     # username = request.user,
#     profile_context = {

#         "profile": user,
#         # "first_name": User.objects.get(username='sani1')
#     }
#     return render(request, "accounts/profile.html", profile_context)


# @login_required
# def profile_project_view(request, *args, **kwargs):
#     qs = Showcase.objects.all()
#     context = {
#         "object_list": qs,

#     }
#     return render(request, "accounts/list.html", context)
