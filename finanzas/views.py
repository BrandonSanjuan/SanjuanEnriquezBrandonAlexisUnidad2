from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MovimientoForm
from .models import Movimiento


@login_required(login_url='/cuentas/login/')
def inicio(request):
    movimientos = Movimiento.objects.filter(
        usuario=request.user
    ).order_by('-fecha', '-id')

    ingresos = sum(
        movimiento.monto
        for movimiento in movimientos
        if movimiento.tipo == 'ingreso'
    )

    gastos = sum(
        movimiento.monto
        for movimiento in movimientos
        if movimiento.tipo == 'gasto'
    )

    saldo = ingresos - gastos

    return render(
        request,
        'finanzas/inicio.html',
        {
            'movimientos': movimientos,
            'ingresos': ingresos,
            'gastos': gastos,
            'saldo': saldo,
        }
    )


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

@login_required(login_url='/cuentas/login/')
def eliminar_movimiento(request, id):
    movimiento = Movimiento.objects.get(
        id=id,
        usuario=request.user
    )

    movimiento.delete()

    return redirect('inicio')