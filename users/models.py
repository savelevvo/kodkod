from django.contrib.auth.models import AbstractUser
from django.db import models


class AuthUser(AbstractUser):
    NA = 3
    USER_GENDER = (
        (1, 'Male'),
        (2, 'Female'),
        (NA, 'Not specified')
    )
    birth_date = models.DateField(null=True, blank=True)
    country_iso = models.CharField(null=True, blank=True, max_length=8)
    verify_email = models.BooleanField(default=False)
    gender = models.SmallIntegerField(choices=USER_GENDER, default=NA)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
