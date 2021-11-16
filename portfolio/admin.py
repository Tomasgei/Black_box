from django.contrib import admin
from . import models
# Register your models here.



admin.site.register(models.StockTicker )
admin.site.register(models.PortfolioStock)