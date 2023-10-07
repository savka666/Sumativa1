from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    resultado = None  # Initialize resultado
    if request.method == "POST":
        numero1 = float(request.POST.get("numero1", 0))
        numero2 = float(request.POST.get("numero2", 0))
        operacion = request.POST.get("operacion")
        resultado = calcular_resultado(numero1, numero2, operacion)
    
    return render(request, "home.html", {"resultado": resultado})

def calculadora(request):
    resultado = None  # Initialize resultado
    if request.method == "POST":
        numero1 = float(request.POST.get("numero1", 0))
        numero2 = float(request.POST.get("numero2", 0))
        operacion = request.POST.get("operacion")
        resultado = calcular_resultado(numero1, numero2, operacion)
    
    if resultado is not None:
        return render(request, "home.html", {"resultado": resultado})
    else:
        return HttpResponse("Error en la operacion")

def calcular_resultado(numero1, numero2, operacion):
    if operacion == "suma":
        return numero1 + numero2
    elif operacion == "resta":
        return numero1 - numero2
    elif operacion == "multiplicacion":
        return numero1 * numero2
    elif operacion == "division":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "No se puede dividir por cero"
    else:
        return "Operacion no valida"



