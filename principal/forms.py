from django import forms
from principal.models import Aluno

class AlunoForm(forms.ModelForm):

    class Meta:
        model=Aluno
        fields = '__all__'

        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'datanascimento': forms.TimeInput(attrs={'type' : 'date'})
        }