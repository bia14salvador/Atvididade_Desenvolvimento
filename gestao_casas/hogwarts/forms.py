from django.forms import ModelForm
from .models import Aluno, Casa

class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = ['nome', 'responsavel']

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'casa']
