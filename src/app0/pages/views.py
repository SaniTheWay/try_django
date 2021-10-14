from django.shortcuts import render
# httpresponse class added to the view
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# from forms import RawShowcaseForm
# Create your views here.
'''
#What HttpResponse is?
-
    HttpResponse provides an inbound HTTP request
    to a Django web application with a text response. 
    This class is most frequently used as a return object from a Django view.

'''


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # return HttpResponse("<h1>Hello Sanidhya Dave!</h1>")  # string of HTML code
    return render(request, "home.html", {})


def projects_view(request, *args, **kwargs):
    print(args, kwargs)
    # return HttpResponse("projects.html")  # string of HTML code
    return render(request, "projects.html", {})


def about_view(request, *args, **kwargs):
    print(request, args, kwargs)
    my_context = {
        'my_name': "sanidhya",
        'my_number': 60205219115,
        'my_data': 'this is my data.',
        'my_list': ['Aaloo', 'papad', 'rawa']
    }
    return render(request, "about.html", my_context)

    # return HttpResponse("about.html")  # string of HTML code


def contact_view(request, *args, **kwargs):
    print(request, args, kwargs)
    print(request.user)
    return render(request, "contact.html", {})
# return HttpResponse("contact.html")  # string of HTML code


@login_required
def profile_view(request, *args, **kwargs):
    print(request, args, kwargs)
    print(request.user)
    profile_context = {
        "user_name": request.user,


    }
    return render(request, "profile.html", profile_context)
