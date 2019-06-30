from enderecos.models import Endereco
from rest_framework.viewsets import ModelViewSet
from .serializers import EnderecoSerializer

class EnderecosViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

