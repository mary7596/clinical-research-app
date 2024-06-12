from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import viewsets
from .models import Study, Patient
from .serializers import StudySerializer, PatientSerializer

class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer