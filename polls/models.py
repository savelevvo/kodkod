from django.db import models
from django.contrib.postgres.fields import JSONField
from users.models import AuthUser


class Poll(models.Model):
    subject = models.CharField(max_length=256)
    description = models.TextField(blank=True, default='')
    constraints = JSONField(default=dict, blank=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
    # todo: tags

    created_timestamp = models.DateTimeField(auto_now_add=True)
    modified_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class Vote(models.Model):
    text = models.CharField(max_length=256)
    votes_number = models.PositiveIntegerField(default=0)
    poll = models.ForeignKey(Poll, related_name='votes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} :: {self.votes_number}'
