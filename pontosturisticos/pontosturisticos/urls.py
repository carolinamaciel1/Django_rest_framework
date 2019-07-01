"""pontosturisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf.urls.static import static
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecosViewSet
from comentarios.api.viewsets import ComentariosViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet

router = routers.DefaultRouter()
router.register('pontosturisticos',PontoTuristicoViewSet,base_name='PontoTuristico')
router.register('atracoes',viewset=AtracaoViewSet)
router.register('enderecos',viewset=EnderecosViewSet)
router.register('comentarios',viewset=ComentariosViewSet)
router.register('avaliacoes',viewset=AvaliacoesViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
