import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from apps.aluno.api.serializers import AlunoSerializer
from apps.aluno.models import Aluno


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'nome']

    @action(methods=['get'], detail=False)
    def pendente(self, request):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)