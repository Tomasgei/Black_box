from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Dashboard_view(request):
    context = {}
    return render(request,"tradingapp/dashboard.html",context )