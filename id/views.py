from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def temp1(request):
    return render(request,"temp1.html")
def base(request):
    return render(request,"base.html")