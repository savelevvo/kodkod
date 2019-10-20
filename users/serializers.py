from rest_framework import serializers
from .models import AuthUser


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('id', 'last_login', 'username', 'first_name', 'last_name', 'email',
                  'date_joined', 'birth_date', 'country_iso', 'verify_email', 'gender')
