# forms.py
from django import forms

from .models import ContactMessage

class BuyNowForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))





class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone_number', 'email', 'message']


class ProductPurchaseForm(forms.Form):
    product_name = forms.CharField(label='Product Name', max_length=100)
    product_price = forms.DecimalField(label='Product Price', max_digits=10, decimal_places=2)

