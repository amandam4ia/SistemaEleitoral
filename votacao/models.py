from django.db import models

# Create your models here.
class Usuario(models.Model):
    matricula = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)
    
    class Meta:
        abstract = True

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

class Administrador(Usuario):
    pass

class Eleitor(Usuario):
    pass

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
    eleitor = models.ForeignKey(Eleitor, on_delete=models.CASCADE, related_name="votos")
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE, related_name="votos")
    chapa = models.ForeignKey(Chapa, on_delete=models.CASCADE, related_name="votos")
    data_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["eleitor", "eleicao"], name="unique_voto_por_eleicao")
        ]

    def __str__(self):
        return f"{self.eleitor.matricula} votou na {self.chapa.nome} ({self.eleicao.titulo})"
