from django.db import models
from django.conf import settings
from django.db.models import Count
# Create your models here.

class Eleicao(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('encerrada', 'Encerrada'),
        ('apurada', 'Apurada'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    data_termino = models.DateTimeField()
    vencedor = models.ForeignKey(
        'Chapa',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='eleicoes_vencidas'
    )

    def __str__(self):
        return self.titulo
    
    def contagem_votos(self):
        """Retorna um dicionário com a contagem de votos por chapa"""
        from .models import Voto  # evita import circular
        votos = (
            Voto.objects
            .filter(eleicao=self)
            .values('chapa__nome')  # ou outro campo da Chapa que identifique
            .annotate(total=Count('id'))
            .order_by('-total')
        )
        soma_total = sum(item['total'] for item in votos)
        return soma_total
        
    def calcular_vencedor(self):
        """Define a chapa vencedora com base na contagem de votos"""
        from .models import Voto

        resultado = (
            Voto.objects
            .filter(eleicao=self)
            .values('chapa')
            .annotate(total=Count('id'))
            .order_by('-total')
        )

        if resultado.exists():
            chapa_id = resultado[0]['chapa']
            from .models import Chapa
            self.vencedor = Chapa.objects.get(pk=chapa_id)
            self.status = 'apurada'
            self.save()
            return self.vencedor
        return None

class Chapa(models.Model):
    nome = models.CharField(max_length=50)
    coordenador = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE, related_name='chapas')

    def __str__(self):
        return self.nome

    @property
    def qtd_votos(self):
        return self.votos.count()
    
    @property
    def foi_eleita(self):
        return self == self.eleicao.vencedora

class Voto(models.Model):
    eleitor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)
    chapa = models.ForeignKey(Chapa, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["eleitor", "eleicao"], name="unique_voto_por_eleicao")
        ]

    def __str__(self):
        return f"{self.eleitor.matricula} votou na {self.chapa.nome} ({self.eleicao.titulo})"
