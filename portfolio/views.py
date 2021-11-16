from django.shortcuts import render, redirect
import pandas_datareader as web
from datetime import datetime
from django.contrib import messages
from .  forms import PortfolioForm
from . models import PortfolioStock
import requests
import json

# Create your views here.
"""
def Portfolio_View(request):
    api_key = "UCWMLBFFC93JMGGL"
    portfolio_list = ["AAPL","FB","BTU","AMC","SPY"] #get tickers from portfolio model
    stock_data = []
    for s in portfolio_list:
        data = web.DataReader(s, "av-daily",api_key=api_key)
        stock_data.append(data)
    context = {"stock_data":stock_data}
    return render(request,"portfolio.html", context )
"""

# Portfolio page
def Portfolio_View(request):
    '''
    Function based view with some api and database queries
    Render porfolio page with table, where you can add or delete stock to portfolio and pull some data for ticker from api
   
    '''

    if request.method == "POST":
        form = PortfolioForm(request.POST or None)
        if  form.is_valid():
            form.save()
            messages.success(request, "Stock Has Been Added To Portfolio")
            return redirect(Portfolio_View)

    else:
        output = [] #temporary save data from api call
        ticker = PortfolioStock.objects.order_by("-id").all()
        

        for ticker_item in ticker:
            base_url = "https://cloud.iexapis.com/stable/stock/"+str(ticker_item)+"/quote?token=pk_e3fa0c44f3714325960230ada76fba10"
            api_request = requests.get(base_url)   
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error...."
    mylist = zip(ticker, output)
    context = {'mylist': mylist}

    return render(request,"portfolio/portfolio.html", context)


def delete(request, stock_id):
    '''
    Function to delete item from portfolio database
    Deletes item from portfolio database based on id
   
    '''
    item = PortfolioStock.objects.get(pk = stock_id )
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect(Portfolio_View)
