from django.db import models
from django.urls import reverse

from django.utils import timezone

from datetime import datetime, timedelta


class Client(models.Model):
    """Name of the end client the terminology is associated to.
    """
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    ) 
    name = models.CharField(
        max_length=100,
    )
    abbr = models.Charfield(
        max_length=10,
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    @property
    def full_name(self):
        """Returns the full name representation of the client company
        including its parent company name.
        """
        return self.parent + ' ' + self.name

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        """Human-readable string representation for validation."""
        return self.name

    def get_absolute_url(self):
        return reverse("termbase:view-clients", kwargs={"pk": self.pk})
    


class Topic(models.Model):
    pass


class Domain(models.Model):
    pass


class Term(models.Model):
    KNOWLEDGE_TYPE = ()
    REGISTER = ()
    pass