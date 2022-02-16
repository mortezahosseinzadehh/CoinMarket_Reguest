from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .bit_price import response, context
# Create your views here.

def home(request):

    return render(request, "blog/home.html", context)
