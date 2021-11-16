from django.db import models

# Create your models here.
class StockTicker(models.Model):
    '''
    This model creating fields for stock to held
    historical data for calculation in tradingapp features
   
    '''
    Ticker  = models.CharField(max_length=10)
    Date    = models.DateField(primary_key=True)
    Open   = models.FloatField()
    High   = models.FloatField()
    Low    = models.FloatField()
    Close  = models.FloatField()
    Volume = models.IntegerField(max_length=20)

    def __str__(self):
        return str(self.name)
        
    class Meta:
        ordering = ['Ticker']

class PortfolioStock(models.Model):
    '''
    This model creating fields for stock in 
    portfolio feature in portfolio page
   
    '''
    Ticker           = models.CharField(max_length=10)
    Qty              = models.IntegerField(max_length=10, verbose_name= "Shares")
    Entry_Date       = models.DateField()
    Current_Price    = models.FloatField()
    Entry_Value      = models.FloatField()
    Current_Value    = models.FloatField()
    
    def __str__(self):
        return str(self.Ticker)
        
    class Meta:
        ordering = ['Ticker']