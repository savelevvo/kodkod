from rest_framework.viewsets import ModelViewSet

from .serializers import PollSerializer
from .models import Poll


class PollView(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
