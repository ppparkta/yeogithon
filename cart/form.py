from django import forms
from .models import Cart
from cartProduct.models import CartProduct

class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ['cartProductCount', 'cartProduct', 'cartProductTemp']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['productTemp'].widget = forms.RadioSelect(choices=[(True, '차가운 음료'), (False, '따뜻한 음료')])

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['cartRequest']