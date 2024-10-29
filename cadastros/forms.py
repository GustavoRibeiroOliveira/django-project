from django import forms
from django.core.exceptions import ValidationError

from cadastros.models import Cidade


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        # fields = ['nome', 'capital']
        fields = '__all__'

    # método de validação do form (form.is_valid)
    def clean(self):

        nome = self.cleaned_data['nome']
        if nome == 'Itajubá':
            raise ValidationError({"nome": "Não podemos cadastrar a cidade de Itajubá no sistema!"})
