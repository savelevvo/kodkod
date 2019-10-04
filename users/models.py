from django.contrib.auth.models import AbstractUser
from django.db import models


class AuthUser(AbstractUser):
    NA = 3
    USER_SEX = (
        (1, 'Male'),
        (2, 'Female'),
        (NA, 'Not specified')
    )
    birth_date = models.DateField(null=True, blank=True)
    country_iso = models.CharField(null=True, blank=True, max_length=8)
    verify_email = models.BooleanField(default=False)
    sex = models.SmallIntegerField(choices=USER_SEX, default=NA)

