from django.shortcuts import render

# importing showcase form to add into the view
from .forms import ShowcaseForm

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


def show_form_view(request):
    context = {}
    return render(request, 'showcase/create.html', context)


# def show_form_view(request):
#     form = ShowcaseForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=ShowcaseForm()

#     context = {
#         'form' : form
#     }
#     return render(request, 'showcase/create.html', context)
