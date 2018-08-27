from django.db import models
import eav
from django.utils import timezone


class RiskType(models.Model):
    """A model class used for storing data
    about risk types
    """
    name = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


eav.register(RiskType)
