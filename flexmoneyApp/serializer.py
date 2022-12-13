from .models import Yoga_Class_Data
from rest_framework import serializers

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yoga_Class_Data
        fields = "__all__"
