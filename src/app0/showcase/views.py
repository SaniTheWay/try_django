from django.shortcuts import render
from django.http import HttpResponseRedirect

# importing showcase form to add into the view
from .forms import RawShowcaseForm, ShowcaseForm, TestForm

# Showcase is a class in models module
from .models import Showcase

# Create your views here.


def showcase_detail_view(request):

    obj = Showcase.objects
# here if I put id=1 then it will show the product having ID-1
    # obj = Showcase.objects.get(id=2)
    # items = list(obj.all())
    # count_obj = len(obj.all()) #no. of showcase objects
    # get_obj = obj.get(id=1)
    context = {
        # 'title' : get_obj.title,
        # 'description' : get_obj.description,
        # 'price' : get_obj.price,
        # 'active' : get_obj.active,
        # 'summary': get_obj.summary,
        # 'featured': get_obj.featured

        "all_projects": obj.all()
    }
    # return render(request, "template", {context})
    return render(request, "showcase/detail.html", context)

    # Creating the View - for Forms

# this will just give us a url (wala khel) : It used in RAW HTMLs

# Pure Django Forms: These are the best one.


def show_form_view(request):

    myform = RawShowcaseForm() #if we get the GET request for the form
    if request.method =="POST": #by using this, we validate if the request is a "Post" request
        # <<NOT CLEAR>>to make this form connected to the DB we have to put 
        #  <<NOT CLEAR>>"request.POST" as parameter of "RawShowcaseForm()"
        myform = RawShowcaseForm(request.POST)
        if myform.is_valid():
            # Now the date is good
            print(myform.cleaned_data) #.cleaned_data - only shows the valid data
            # saving the object to the DB
            Showcase.objects.create(**myform.cleaned_data) #made "myform.cleaned_data" as an argument for the 'create()' mehthod
            myform = RawShowcaseForm()

        else:
            print(myform.errors) #.errors - shows the data that is having errors/invalid
    context = {
        'form':myform
    }
    return render(request, 'showcase/create.html', context)

# -----------------------------------------------------------------------------------------------------------
# practice forms
# def testingformview(request):
#     # if request.method == "POST":
#     #     form = TestForm(request.POST)
#     #     if form.is_valid():
#     #         return HttpResponseRedirect('/showcase/')
#     # else:
#     # form = TestForm()q
#     context= {
#         'form': TestForm(request.GET)
#         }
#     return render(request, 'showcase/create.html', context) 
# -----------------------------------------------------------------------------------------------------------

# def show_form_view(request):

#     print(request.GET)
#     print(request.POST)
#     # validating the data:
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         #Showcase.objects.create(myform.cleaned_data) to create the object- really
#     context = {}
#     return render(request, 'showcase/create.html', context)


# def show_form_view(request):
#     form = ShowcaseForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=ShowcaseForm()

#     context = {
#         'form' : form
#     }
#     return render(request, 'showcase/create.html', context)
