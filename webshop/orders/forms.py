from django import forms

class OrderForm(forms.Form):
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес доставки'}),
        label='Адрес доставки'
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите контактный телефон'}),
        label='Контактный телефон'
    )