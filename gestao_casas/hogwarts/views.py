from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Casa
from .forms import AlunoForm, CasaForm

def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno_list.html', {'alunos': alunos})

def aluno_create(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, 'aluno_form.html', {'form': form})

def aluno_update(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, 'aluno_form.html', {'form': form})

def aluno_delete(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('aluno_list')
    return render(request, 'aluno_confirm_delete.html', {'aluno': aluno})

def casa_list(request):
    casa = Casa.objects.all()
    return render(request, 'casa_list.html', {'casa': casa})

def casa_create(request):
    form = CasaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('casa_list')
    return render(request, 'casa_form.html', {'form': form})

def casa_update(request, id):
    casa = get_object_or_404(Casa, id=id)
    form = CasaForm(request.POST or None, instance=casa)
    if form.is_valid():
        form.save()
        return redirect('casa_list')
    return render(request, 'casa_form.html', {'form': form})

def casa_delete(request, id):
    casa = get_object_or_404(Casa, id=id)
    if request.method == 'POST':
        casa.delete()
        return redirect('casa_list')
    return render(request, 'casa_confirm_delete.html', {'casa': casa})
