from .models import Eleicao, Voto, Chapa
from usuarios.models import Usuario
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EleicaoForm, ChapaForm

def is_admin(user):
    return user.is_staff or user.is_superuser


# ---------------------- ELEIÇÃO ----------------------

@login_required
def criar_eleicao(request):
    if request.method == "POST":
        form = EleicaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Eleição criada com sucesso!")
            return redirect("dashboard")
    else:
        form = EleicaoForm()
    return render(request, "eleicao/criar_eleicao.html", {"form": form})


@login_required
def editar_eleicao(request, eleicao_id):
    eleicao = get_object_or_404(Eleicao, pk=eleicao_id)
    if request.method == "POST":
        form = EleicaoForm(request.POST, instance=eleicao)
        if form.is_valid():
            form.save()
            messages.success(request, "Eleição atualizada com sucesso!")
            return redirect("ver_eleicao", eleicao_id=eleicao_id)
    else:
        form = EleicaoForm(instance=eleicao)
    return render(request, "eleicao/editar_eleicao.html", {"form": form, "eleicao": eleicao})


@login_required
def ver_eleicao(request, eleicao_id):
    eleicao = get_object_or_404(Eleicao, pk=eleicao_id)
    chapas = eleicao.chapas.all()
    return render(request, "eleicao/ver_eleicao.html", {"eleicao": eleicao, "chapas": chapas})


@login_required
def deletar_eleicao(request, eleicao_id):
    eleicao = get_object_or_404(Eleicao, pk=eleicao_id)
    if request.method == "POST":
        eleicao.delete()
        messages.success(request, "Eleição excluída com sucesso!")
        return redirect("dashboard")
    return render(request, "eleicao/deletar_eleicao.html", {"eleicao": eleicao})


# ---------------------- CHAPA ----------------------

@login_required
def criar_chapa(request):
    if request.method == "POST":
        form = ChapaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Chapa criada com sucesso!")
            return redirect("dashboard")
    else:
        form = ChapaForm()
    return render(request, "eleicao/criar_chapa.html", {"form": form})

@login_required
def editar_chapa(request, chapa_id):
    chapa = get_object_or_404(Chapa, pk=chapa_id)
    if request.method == "POST":
        form = ChapaForm(request.POST, instance=chapa)
        if form.is_valid():
            form.save()
            messages.success(request, "Chapa atualizada com sucesso!")
            return redirect("ver_chapa", chapa_id=chapa_id)
    else:
        form = ChapaForm(instance=chapa)
    return render(request, "eleicao/editar_chapa.html", {"form": form, "chapa": chapa})


@login_required
def ver_chapa(request, chapa_id):
    chapa = get_object_or_404(Chapa, pk=chapa_id)
    return render(request, "eleicao/ver_chapa.html", {"chapa": chapa})


@login_required
def deletar_chapa(request, chapa_id):
    chapa = get_object_or_404(Chapa, pk=chapa_id)
    if request.method == "POST":
        chapa.delete()
        messages.success(request, "Chapa excluída com sucesso!")
        return redirect("dashboard")
    return render(request, "eleicao/deletar_chapa.html", {"chapa": chapa})

# ---------------------- DEMAIS TELAS ----------------------

@login_required
def dashboard(request):
    # Estatísticas gerais
    total_eleicoes = Eleicao.objects.count()
    eleicoes_abertas = Eleicao.objects.filter(status="aberta").count()
    votos_usuario = Voto.objects.filter(eleitor=request.user).count()

    # Todas as eleições com suas informações
    eleicoes = Eleicao.objects.all().select_related("vencedor").prefetch_related("chapas")

    context = {
        "total_eleicoes": total_eleicoes,
        "eleicoes_abertas": eleicoes_abertas,
        "votos_usuario": votos_usuario,
        "eleicoes": eleicoes,
    }
    return render(request, "eleicao/dashboard.html", context)


@login_required
def votar(request, eleicao_id):
    votantes = Usuario.objects.all().count()
    eleicao = get_object_or_404(Eleicao, id=eleicao_id)
    chapas = eleicao.chapas.all()

    if request.method == "POST":
        chapa_id = request.POST.get("chapa_id")
        voto_existente = Voto.objects.filter(eleitor=request.user, eleicao=eleicao).exists()
        if voto_existente:
            messages.warning(request, "Você já votou nesta eleição.")
        else:
            chapa = get_object_or_404(Chapa, id=chapa_id)
            Voto.objects.create(eleicao=eleicao, chapa=chapa, eleitor=request.user)
            messages.success(request, f"Seu voto para {chapa.nome} foi registrado!")
            return redirect('dashboard')

    total_votos = Voto.objects.filter(eleicao=eleicao).count()
    participacao = (total_votos / votantes) * 100 if votantes else 0

    context = {
        'eleicao': eleicao,
        'chapas': chapas,
        'total_votos': total_votos,
        'total_eleitores': votantes,
        'participacao': round(participacao, 1),
    }
    return render(request, 'eleicao/votar.html', context)


@login_required
def resultados_eleicao(request, eleicao_id):
    eleicao = get_object_or_404(Eleicao, id=eleicao_id)
    chapas = eleicao.chapas.all()
    total_votos = Voto.objects.filter(eleicao=eleicao).count() or 1

    resultados = []
    for chapa in chapas:
        votos = Voto.objects.filter(eleicao=eleicao, chapa=chapa).count()
        porcentagem = (votos / total_votos) * 100
        resultados.append({
            'chapa': chapa,
            'votos': votos,
            'porcentagem': round(porcentagem, 1)
        })

    resultados.sort(key=lambda x: x['votos'], reverse=True)
    vencedor = resultados[0] if resultados else None

    context = {
        'eleicao': eleicao,
        'resultados': resultados,
        'vencedor': vencedor,
        'total_votos': total_votos
    }
    return render(request, 'eleicao/resultado_eleicao.html', context)

@login_required
def finalizar_eleicao(request, eleicao_id):
    eleicao = get_object_or_404(Eleicao, id=eleicao_id)

    # Só permite finalizar se ainda estiver aberta
    if eleicao.status == 'aberta':
        vencedor = eleicao.calcular_vencedor()
        if vencedor:
            messages.success(request, f"Eleição finalizada! Vencedor: {vencedor.nome}.")
        else:
            messages.warning(request, "Nenhum voto computado. Eleição encerrada sem vencedor.")
    else:
        messages.info(request, "Esta eleição já foi finalizada ou apurada.")

    return redirect('ver_eleicao', eleicao_id=eleicao.id)