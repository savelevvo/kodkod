from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PollSerializer
from .models import Poll, Vote
from django.shortcuts import get_object_or_404


class PollsList(APIView):
    def get(self, request, format=None):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


class PollDetail(APIView):
    def get(self, request, pk, format=None):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    def post(self):
        pass
