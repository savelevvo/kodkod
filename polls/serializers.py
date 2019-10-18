from rest_framework import serializers
from .models import Poll, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('text', 'votes_number')


class PollSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
