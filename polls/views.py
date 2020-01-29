from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from django.db.models.aggregates import Sum

from .serializers import PollSerializer
from .models import Poll


class PollView(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    pagination_class = LimitOffsetPagination

    @action(detail=False)
    def popular(self, request):
        popular = Poll.objects.annotate(c=Sum('votes__votes_number')).order_by('-c')
        page = self.paginate_queryset(popular)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(popular, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def recent(self, request):
        recent = Poll.objects.all().order_by('-id')
        page = self.paginate_queryset(recent)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent, many=True)
        return Response(serializer.data)
