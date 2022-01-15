from django.db import models
import uuid
from django.utils import timezone


# Create your models here.

def hex_uuid():
    return uuid.uuid4().hex


class ApiModel(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    identifier = models.CharField(max_length=32, default=hex_uuid, editable=True)

    def __str__(self):
        # self.id
        return str(self.timestamp)

    class Meta:
        ordering = ('-pk',)

# 2020-07-15 14:30:26.159446
# 2021-05-21 12:10:19.484523
# 2022-01-15 21:50:19+00:00
