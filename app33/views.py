from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hari(request):
    return HttpResponse("<h1><marquee> hii how are you</h1></marquee>")  


def anu(request):
    return HttpResponse("<h1><marquee>i am fine </h1></marquee>")