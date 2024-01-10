from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from django.urls import reverse_lazy


# Define the home view
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# Add new view
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, "finches/index.html", {"finches": finches})


def finches_detail(request, finch_id):
    finch = get_object_or_404(Finch, id=finch_id)
    return render(request, "finches/detail.html", {"finch": finch})


class FinchCreate(CreateView):
    model = Finch
    fields = "__all__"
    success_url = "/finches/"
    template_name = "finches/create.html"


class FinchDelete(DeleteView):
    model = Finch
    success_url = "/finches/"
    template_name = "finches/delete.html"


class FinchUpdate(UpdateView):
    model = Finch
    fields = ["name", "species", "description", "age"]
    template_name = "finches/update.html"
    success_url = "/finches/"
