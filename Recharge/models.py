from django.db import models
from django.contrib.auth.models import User


class Recharge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operator = models.CharField(max_length=10, null=False, blank=False)
    circle = models.CharField(max_length=20, null=False, blank=False)
    number = models.CharField(max_length=10, null=False, blank=False)
    amount = models.CharField(max_length=5, null=False, blank=False)

    def __str__(self):
        return self.number
