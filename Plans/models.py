from django.db import models


class Plans(models.Model):
    Operator = models.CharField(max_length=10, null=False, blank=False)
    Circle = models.CharField(max_length=30, null=False, blank=False)
    Plan_type = models.CharField(max_length=10, null=False, blank=False)
    Data = models.CharField(max_length=20, null=False, blank=False)
    Validity = models.CharField(max_length=30, null=False, blank=False)
    Description = models.CharField(max_length=100, null=False, blank=False)
    Price = models.CharField(max_length=30, null=False, blank=False)



    def __str__(self):
        return self.Plan_type
