# api/serializers.py
from rest_framework import serializers
from .models import Study, Patient

class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'