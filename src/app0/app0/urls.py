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
# from pages import views
# either doing in this way| we can use the below one:
from pages.views import home_view, projects_view, about_view
from showcase.views import showcase_detail_view, show_form_view #jst added the another app view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='landingPage'),
    path('projects/', projects_view,),
    path('about/',  about_view,),
    path('contacts/',  about_view,),
    path('showcase/',  showcase_detail_view,),
    path('create/',  show_form_view,),


]
