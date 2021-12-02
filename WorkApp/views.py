from rest_framework import viewsets
from WorkApp.serializers import LegalSerializer, ClientSerializer, DepartmentSerializer
from WorkApp.models import LegalPerson, Client, Departments


class LegalSet(viewsets.ModelViewSet):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalSerializer


class ClientSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DepartmentSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
