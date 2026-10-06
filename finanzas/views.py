from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MovimientoForm


def inicio(request):
    return render(request, 'finanzas/inicio.html')


@login_required(login_url='/cuentas/login/')
def agregar_movimiento(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)

        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.usuario = request.user
            movimiento.save()

            return redirect('inicio')
    else:
        form = MovimientoForm()

    return render(
        request,
        'finanzas/agregar_movimiento.html',
        {'form': form}
    )