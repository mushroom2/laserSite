from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductsForm(forms.Form):
    quantity = forms.IntegerField(initial=1,
                                  label='Кількість ',
                                  min_value=0)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)