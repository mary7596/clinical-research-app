# api/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import StudyViewSet, PatientViewSet

router = DefaultRouter()
router.register(r'studies', StudyViewSet)
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]