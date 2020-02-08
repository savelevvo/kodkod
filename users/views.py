from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.serializers import AuthUserSerializer
from polls.serializers import PollSerializer

from users.models import AuthUser
from polls.models import Poll
from .forms import RegistrationForm


class AuthUserView(ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    def get_permissions(self):
        permission_classes = ()
        if self.action in {'retrieve', 'account'}:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

    @action(methods=['post'], detail=False, url_path='create-account', url_name='create-account')
    def create_account(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def polls(self, request, pk):
        serializer = PollSerializer(Poll.objects.filter(user=pk), many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def account(self, request):
        pass
