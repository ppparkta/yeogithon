from django import forms
from .models import Product

# 상품 등록 폼
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('productName', 'productPrice', 'productImage', 'productTemp')