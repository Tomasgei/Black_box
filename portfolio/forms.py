from django import forms
from . models import PortfolioStock

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortfolioStock
        fields = ["Ticker","Qty","Entry_Date","Current_Price","Entry_Value","Current_Value"]