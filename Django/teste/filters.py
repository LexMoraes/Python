from multiprocessing.connection import Client

from django_filters import rest_framework as filters

from tecommerce.teste.models import Product, Sale, Employee

# Filtros de pesquisa
LIKE = 'unaccent__icontains'
EQUALS = 'exact'
STARTS_WITH = 'startswith'

class ClientViewSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    rg = filters.CharFilter(lookup_expr=EQUALS)
    age = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = Client
        fields = ['name', 'rg', 'age']

class ProductViewSet(filters.FilterSet):
    description = filters.CharFilter(lookup_expr=LIKE)
    quanty = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = Product
        fields = ['description', 'quanty']

class SaleViewSet(filters.FilterSet):
    nrf = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = Sale
        fields = ['name', 'nrf']

class EmployeeViewSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    registraction = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = Employee
        fields = ['name', 'registraction']
