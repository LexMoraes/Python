from rest_framework import serializers

from tecommerce.teste.models import Cliente, Product, Sale, Employee


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True, max_length=80)
    age = serializers.IntegerField(read_only=True, min_value=0, max_value=100)
    class Meta:
        model = Cliente
        fields = ['id', 'created_at', 'modified_at', 'name', 'active', 'name', 'rg']

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True, max_length=80)
    price = serializers.IntegerField(read_only=True, min_value=0, max_value=100)
    class Meta:
        model = Product
        fields = ['id', 'created_at', 'modified_at', 'name', 'price']

class SaleSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Sale
        fields = ['id', 'name', 'registration']

class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True, max_length=80)
    class Meta:
        model = Employee
        fields = ['id', 'created_at', 'modified_at']
