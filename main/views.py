from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CalificacionForm
from .models import Calificacion
def pagina_principal(request):
    return render(request, 'main.html')

def alumnos(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'alumnos.html', {'calificaciones': calificaciones})

def profesores(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesores')  # Redirige a la página de profesores después de agregar la calificación
    else:
        form = CalificacionForm()
    return render(request, 'profesores.html', {'form': form})
