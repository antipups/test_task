from WorkApp.models import LegalPerson, Client, Departments
from rest_framework import serializers


class LegalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LegalPerson
        fields = '__all__'


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
