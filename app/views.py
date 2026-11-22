from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import F


class ProductListCreateApiView(ListCreateAPIView):
    """
    View adatpada pra aceitar lista de dados em apenas um POST
    """
    queryset = Product.objects.all().order_by("name")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=201)


class ProductUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'uuid'
    permission_classes = [IsAuthenticated]

class MovimentationListCreateAPIView(ListCreateAPIView):
    queryset = Movimentation.objects.all()
    serializer_class = MovimentationSerializer
    permission_classes = [IsAuthenticated]

class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

# views adicionais

class AbaixoDoMinimoListAPIView(ListAPIView):
    queryset = Product.objects.filter(stock__lt=F('min_stock')).order_by("name")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]