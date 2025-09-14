from django.contrib import admin
from .models import Eleicao, Eleitor, Chapa

# Register your models here.
@admin.register(Eleicao)
class EleicaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data_termino')

@admin.register(Chapa)
class ChapaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'coordenador')