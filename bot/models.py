from django.db import models


class Groups(models.Model):
    group_id = models.CharField(max_length=100, null=True, blank=True)
    

