"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from votacao.views import *
from usuarios.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('votar/<int:eleicao_id>/', votar, name='votar'),
    path('resultados/<int:eleicao_id>/', resultados_eleicao, name='resultados'),
    path('usuarios/', include('usuarios.urls')),

    path("eleicao/criar/", criar_eleicao, name="criar_eleicao"),
    path("eleicao/<int:eleicao_id>/", ver_eleicao, name="ver_eleicao"),
    path("eleicao/<int:eleicao_id>/editar/", editar_eleicao, name="editar_eleicao"),
    path("eleicao/<int:eleicao_id>/deletar/", deletar_eleicao, name="deletar_eleicao"),

    path("chapa/criar/", criar_chapa, name="criar_chapa"),
    path("chapa/<int:chapa_id>/", ver_chapa, name="ver_chapa"),
    path("chapa/<int:chapa_id>/editar/", editar_chapa, name="editar_chapa"),
    path("chapa/<int:chapa_id>/deletar/", deletar_chapa, name="deletar_chapa"),

    path('eleicao/finalizar/<int:eleicao_id>/', finalizar_eleicao, name='finalizar_eleicao'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)