from django.db import models
from django.contrib.postgres.fields import JSONField


class Poll(models.Model):
    subject = models.CharField(max_length=256)
    tags = models.CharField()
    description = models.TextField(blank=True, default='')
    constraints = JSONField(default=dict())
    user = models.ForeignKey('AuthUser', on_delete=models.SET_NULL)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    modified_timestamp = models.DateTimeField(auto_now=True)


class Vote(models.Model):
    text = models.CharField(max_length=256)
    votes_number = models.PositiveIntegerField(default=0)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
