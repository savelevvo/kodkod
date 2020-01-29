from rest_framework import serializers

from .models import Poll, Vote
from users.serializers import AuthUserSerializer


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('text', 'votes_number')


class PollSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)
    user = AuthUserSerializer(many=False, read_only=True)
    votes_count = serializers.ReadOnlyField()

    class Meta:
        model = Poll
        fields = '__all__'
