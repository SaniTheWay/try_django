from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
# importing showcase form to add into the view
from .forms import ShowcaseForm

# Showcase is a class in models module
from .models import Showcase

# Create your views here.
# ----------------------------CREATE SHOWCASE VIEW-------------------------------------------------------


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

# ----------------------------------------------------------------------------------------
# Creating the View - for Forms

# this will just give us a url (wala khel) : It used in RAW HTMLs

# Pure Django Forms: These are the best one.

# ----------------------------CREATE SHOWCASE VIEW-------------------------------------------------------

# '''
# Class based views
# '''


class createModel_view(LoginRequiredMixin, CreateView):
    form_class = ShowcaseForm
    template_name = 'showcase/create.html'
    success_url = "."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# @login_required
# def createModel_view(LoginRequiredMixin, CreateView):
#     form = ShowcaseForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.created_by = request.user
#         obj.save()
#         form = ShowcaseForm()
#     # else:
#     #     print(form.errors)
#     #     return HttpResponse("Enter Valid Data.")

#     context = {
#         'form': form
#     }
#     return render(request, 'showcase/create.html', context)


# @login_required
# def createform_view(request, *args, **kwargs):
#     myform = RawShowcaseForm()  # if we get the GET request for the form
#     if request.method == "POST":  # by using this, we validate if the request is a "Post" request
#         # <<NOT CLEAR>>to make this form connected to the DB we have to put
#         #  <<NOT CLEAR>>"request.POST" as parameter of "RawShowcaseForm()"
#         myform = RawShowcaseForm(request.POST, request.FILES)
#         if myform.is_valid():
#             # Now the date is good
#             # .cleaned_data - only shows the valid data
#             print(myform.cleaned_data)
#             # saving the object to the DB
#             # made "myform.cleaned_data" as an argument for the 'create()' mehthod
#             Showcase.objects.create(**myform.cleaned_data)
#             myform = RawShowcaseForm()
#             # return HttpResponse("success")
#         else:
#             # .errors - shows the data that is having errors/invalid
#             print(myform.errors)
#     context = {
#         'form': myform
#     }
#     return render(request, 'showcase/create.html', context)
