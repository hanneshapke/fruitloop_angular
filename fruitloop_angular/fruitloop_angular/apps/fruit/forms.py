from django import forms

from .models import FruitLocation


class FruitLocationForm(forms.ModelForm):

    class Meta:
        model = FruitLocation
        fields = (
            'address',
            'fruit_type',
            'comment'
        )
