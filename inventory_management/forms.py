from django import forms

from inventory_management.models import Product,coupon

class inventory_form(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class coupon(forms.ModelForm):

    class Meta:
        model = coupon
        fields = '__all__'