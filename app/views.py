from django.shortcuts import render

# Create your views here.

def Homeview(request):
    context = {}
    return render(request,"home.html",context )
