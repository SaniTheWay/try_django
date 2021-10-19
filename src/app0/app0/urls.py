"""app0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import *
# from pages import views
# either doing in this way| we can use the below one:
from accounts.views import profile_view, profile_project_view
from pages.views import home_view, projects_view, about_view
# show_form_view #jst added the another app view
from showcase.views import showcase_detail_view, createform_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='landingPage'),
    path('dashboard/', home_view,),
    # path('projects/', projects_view,),
    path('about/',  about_view,),
    path('contacts/',  about_view,),
    path('showcase/',  showcase_detail_view,),
    path('create/', createform_view,),
    path('profile/<str:user>/', profile_view, name='userprofile'),
    # path('profile/(?P<username>.+)/$', profile_view, name='userprofile'),

    path('register/', register_view,),
    path('login/', login_view,),
    path('logout/', logout_view,),
    path('projects/', profile_project_view,),



]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
