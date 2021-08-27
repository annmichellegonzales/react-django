from leads.models import Lead
from rest_framework import serializers, viewsets, permissions
from .serializers import LeadSerializer

#Lead Viewset (CRUD)

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class =LeadSerializer