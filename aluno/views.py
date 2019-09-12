
from django.shortcuts import render, redirect
from . models import Aluno
from . forms import AlunoForm


def aluno_list (request):
    alunos=Aluno.objects.all()
    return render(request, 'list.html', {'alunos': alunos})

def aluno_show(request, aluno_id):
    aluno=Aluno.objects.get(pk=aluno_id)
    return render(request, 'show.html', {'aluno':aluno})
    

def aluno_form(request):
    if (request.method == 'POST'):
        form = AlunoForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect ('/aluno/alunos/')
        else:
            return render(request, 'form.html', {'form':form})  
       
    else:
        form = AlunoForm()
        return render(request, 'form.html', {'form': form})       

def excluir_aluno(request, aluno_id):
          aluno=Aluno.objects.get(pk=aluno_id)
          aluno.delete()
          return redirect ('/aluno/alunos/')

def editar_aluno (request, aluno_id):
     if (request.method == 'POST'):
        aluno=Aluno.objects.get(pk=aluno_id)
        form = AlunoForm(request.POST, instance = aluno)
        if form.is_valid():
             form.save()
             return redirect ('/aluno/alunos/')
        else: 
             return render (request, 'editar.html', {'form':form, 'aluno_id': aluno_id})
    
     else:
         aluno=Aluno.objects.get(pk=aluno_id)    
         form = AlunoForm(instance = aluno)
         return render (request, 'editar.html', {'form':form, 'aluno_id': aluno_id})
             

         


# Create your views here.
