from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from drf_yasg.utils import swagger_auto_schema


from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



from djoser.views import UserViewSet

class UserSet(UserViewSet):
    def activation(self, request, *args, **kwargs):
        return super().activation(request, *args, **kwargs)