from django import forms
from .models import Movimiento


class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = [
            'concepto',
            'monto',
            'tipo',
            'categoria',
            'fecha',
            'descripcion',
        ]

        widgets = {
            'fecha': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'descripcion': forms.Textarea(
                attrs={'rows': 3}
            ),
        }