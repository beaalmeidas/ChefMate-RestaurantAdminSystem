from django import forms
from .models import FoodItem_Model


class Meta:
    model = FoodItem_Model
    fields = '__all__'
    widgets = {
        'item_id': forms.NumberInput(attrs={'readonly': 'readonly'}),
        'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'}),
        'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'price', 'step': '0.01'}),
        'category': forms.TextInput(attrs={'class': 'form-control', 'id': 'category'}),
    }
    labels = {
        'item_id': 'ID do Item',
        'name': 'Nome do Item',
        'description': 'Descrição do Item',
        'price': 'Preço',
        'category': 'Categoria do Item'
    }
