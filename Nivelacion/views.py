from django.shortcuts import render, redirect
from .forms import RegistroMateriaForm
from .models import RegistroMateria

def agregar_y_listar_materias(request):
    if request.method == 'POST':
        form = RegistroMateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_materias')  
    else:
        form = RegistroMateriaForm()

    registros = RegistroMateria.objects.order_by('-fecha_registro')

    return render(request, 'Nivelacion/lista_materias.html', {
        'form': form,
        'registros': registros
    })
