from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    var_nome = request.POST.get("nome")
    Pessoa.objects.create(nome=var_nome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id = id)
    return render (request, "update.html", {"pessoa": pessoa})

def update(request, id):
    var_nome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = var_nome
    pessoa.save()
    return redirect(home)
    