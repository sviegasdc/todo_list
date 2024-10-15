from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ListaForm
from .models import Lista

# Create your views here.

def index(request):
    item_list = Lista.objects.order_by('word')
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('lista')
    form = ListaForm()

    page = {
        "forms": form,
        "list" : item_list, 
        "title" : "LISTA DE COMPRAS"
    }
    return render(request, 'lista/index.html', page)

def remove(request, id_item):
    mercadoria = Lista.objects.get(id=id_item)
    mercadoria.delete()
    messages.info(request, "Item removido!")
    return redirect('lista')