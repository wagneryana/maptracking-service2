from ..models.facultad import Facultad
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class FacultadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Facultad
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(FCE__icontains=query),
                    Q(FIA__icontains=query),
                    Q(FCHE__icontains=query),
                    Q(FCS__icontains=query),
                    Q(FT__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
