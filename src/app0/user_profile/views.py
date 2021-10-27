from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.
from showcase.models import Showcase
from user_profile.models import User_profile


User = get_user_model()


@login_required(redirect_field_name='projectyverse')
def profile_view(request, *args, **kwargs):
    user = User.objects.get(email=request.user)
    profile = User_profile.objects.get(user=request.user)
    # username = request.user,
    profile_context = {

        "user": user,
        "profile": profile,
        # "first_name": User.objects.get(username='sani1')
    }
    return render(request, "profile.html", profile_context)


@login_required
def profile_project_view(request, *args, **kwargs):
    qs = Showcase.objects.all()
    context = {
        "object_list": qs,
    }
    return render(request, "accounts/list.html", context)
