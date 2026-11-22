from rest_framework import serializers,status
from .models import *
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def validate(self, data):
        min_stock = data.get("min_stock")

        if min_stock is not None and min_stock < 0:
            raise ValidationError({"min_stock": "min_stock não pode ser negativo."})

        return data


class MovimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movimentation
        fields = "__all__"

    def create(self, validated_data):
        movimementation = validated_data.get('type')
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')

        if movimementation == 'output':
            if quantity <= 0:
                raise ValidationError("A quantidade deve ser maior que zero para movimentações de saída")
            if product.stock == 0:
                raise ValidationError("Estoque insuficiente. O produto está zerado.")
            if product.stock - quantity < 0:
                raise ValidationError("Quantidade maior que o estoque disponível")
            product.stock -= quantity
        elif movimementation == 'input':
            if quantity <= 0:
                raise ValidationError("A quantidade deve ser maior que zero para movimentações de entrada")
            product.stock += quantity
        else:
            raise ValidationError("Tipo de movimentação inválido")

        product.save()

        return super().create(validated_data)

class LoginSerializer(TokenObtainPairView):
    def validate(self,attrs):
        data = super().validate(attrs)

        data['user'] = {
            'username':self.user.username,
            'email':self.user.email
        }

        return data

