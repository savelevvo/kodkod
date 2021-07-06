from rest_framework import serializers
from .models import AuthUser
from polls.models import Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class AuthUserSerializer(serializers.ModelSerializer):
    polls = PollSerializer(many=True, read_only=True)

    class Meta:
        model = AuthUser
        fields = ('id', 'last_login', 'username', 'first_name', 'last_name', 'email',
                  'date_joined', 'birth_date', 'country_iso', 'verify_email', 'gender', 'polls')
