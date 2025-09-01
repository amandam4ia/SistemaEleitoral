from django.db import models

# Create your models here.
class Administrador(models.Model):
    matricula = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    adm = True

class Eleicao(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    data_termino = models.DateTimeField()

    def __str__(self):
        return self.titulo

class Chapa(models.Model):
    nome = models.CharField(max_length=50)
    coordenador = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    qtd_votos = models.IntegerField()
    eleita = models.BooleanField()
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE, related_name='chapas')

    def __str__(self):
        return self.nome

class Eleitor(models.Model):
    matricula = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    adm = False

    def __str__(self):
        return self.matricula

class Voto(models.Model):
    eleitor = models.ForeignKey(Eleitor, on_delete=models.CASCADE, related_name="votos")
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE, related_name="votos")
    chapa = models.ForeignKey(Chapa, on_delete=models.CASCADE, related_name="votos")
    data_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("eleitor", "eleicao")

    def __str__(self):
        return f"{self.eleitor.nome} votou na {self.chapa.nome} ({self.eleicao.titulo})"