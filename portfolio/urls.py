
from django.urls import path, include
from . views import Portfolio_View,delete

urlpatterns = [
    path("portfolio/", Portfolio_View , name = "portfolio" ),
    path("delete/<stock_id>", delete, name = "delete"),      
]
