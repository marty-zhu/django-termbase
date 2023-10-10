from django.db import models
from django.urls import reverse

from django.utils import timezone
from django.utils import gettext as _

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
        if self.parent:
            return self.parent + ' ' + self.name
        else:
            self.name

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        """Human-readable string representation for validation."""
        return self.name

    def get_absolute_url(self):
        return reverse("termbase:view-client", kwargs={"pk": self.pk})
    


class Topic(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        """Human-readable string representation for validation."""
        return self.name


class Domain(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        """Human-readable string representation for validation."""
        return self.name


class Term(models.Model):
    TYPE_CONCEPT = 'c'
    TYPE_FACT = 'f'
    TYPE_PROCEDURE = 'p'

    KNOWLEDGE_TYPE = (
        (TYPE_CONCEPT, 'Concept'),
        (TYPE_FACT, 'Fact'),
        (TYPE_PROCEDURE, 'Procedure')
    )

    REG_LITERARY = 'li'
    REG_FORMAL = 'fo'
    REG_NORMAL = 'no'
    REG_INFORMAL = 'if'
    REG_FAMILIAR = 'fa'
    REG_SLANG = 'sl'
    REGISTER = (
        (REG_LITERARY, 'Literary'),
        (REG_FORMAL, 'Formal'),
        (REG_NORMAL, 'Normal'),
        (REG_INFORMAL, 'Informal'),
        (REG_FAMILIAR, 'Familiar'),
        (REG_SLANG, 'Slang'),
    )

    pass