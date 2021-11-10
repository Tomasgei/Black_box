
from django.urls import path
from . import views as trading_views

urlpatterns = [
    path("tradingapp/dashboard/", trading_views.Dashboard_view, name = "dashboard"),
    path("tradingapp/profile/", trading_views.User_profile_view.as_view(), name = "user_profile"),
]
