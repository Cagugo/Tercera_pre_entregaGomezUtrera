from django import forms
from .models import Mask, SurgicalCap, CustomOrder

class MaskForm(forms.ModelForm):
    class Meta:
        model = Mask
        fields = '__all__'

class SurgicalCapForm(forms.ModelForm):
    class Meta:
        model = SurgicalCap
        fields = '__all__'

class CustomOrderForm(forms.ModelForm):
    class Meta:
        model = CustomOrder
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255)