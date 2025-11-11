from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.conf import settings

class Usuario(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(blank=False)
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True, verbose_name="Foto de Perfil")

    def __str__(self):
        return f"{self.username}"
    
    @property
    def is_administrador(self):
        return self.groups.filter(name="ADMINISTRADORES").exists()
    
    @property
    def is_votante(self):
        return self.groups.filter(name="VOTANTES").exists()

    def has_valid_photo(self):
        if self.foto_perfil and self.foto_perfil.name:
            caminho = os.path.join(settings.MEDIA_ROOT, self.foto_perfil.name)
            return os.path.exists(caminho)
        return False

    def get_photo_url(self):
        if self.has_valid_photo():
            return self.foto_perfil.url
        return None