from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(request, *args, **kwargs):
    return render(request, "pages/home.html", {})