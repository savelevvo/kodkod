from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from users.serializers import AuthUserSerializer
from polls.serializers import PollSerializer

from users.models import AuthUser
from polls.models import Poll


class AuthUserView(ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    @action(methods=['post'], detail=False)
    def register(self, request):
        username, password = request.POST.get('username', ''), request.POST.get('password', '')
        if not username or not password:
            return Response({'error': 'both username and password must be provided'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            user = AuthUser.objects.create(username=username)
            user.set_password(password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def polls(self, request, pk):
        serializer = PollSerializer(Poll.objects.filter(user=pk), many=True)
        return Response(serializer.data)
