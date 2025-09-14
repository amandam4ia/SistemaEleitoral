from django.shortcuts import render

# Create your views here.
def dashboard(request):
    context = {

    }
    return render(request, "eleicao/dashboard.html", context)

def index(request):
    context = {

    }
    return render(request, "eleicao/index.html", context)

def votar(request):
    context = {

    }
    return render(request, "eleicao/votar.html", context)

def resultados(request):
    context = {

    }
    return render(request, "eleicao/resultados.html", context)