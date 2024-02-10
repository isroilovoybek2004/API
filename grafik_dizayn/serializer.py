from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from grafik_dizayn.models import Kurs


class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = '__all__'
