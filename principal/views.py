from django.shortcuts import render
from principal.forms import AlunoForm

def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()
    
    return render(request, 'forms.html', {'form' : form})

