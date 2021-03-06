# -*- coding: utf-8 -*-
"""
Defines the Organization model
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from .contributor import Contributor

# Create your models here.
class Organization(Contributor):
    """
    Definition for Person
    """
    # Relationships

    # Attributes
    abbreviation = models.CharField(max_length=8,
                                    verbose_name='Abbreviation',
                                    null=True,
                                    blank=True)
    # Manager

    # Functions
    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        """
        On save, update timestamps and parameters
        """

        if not self.id or not self.created:
            self.created = timezone.now()
            self.id = slugify(self.name)

        self.modified = timezone.now()
        self.id = slugify(self.name) # pylint: disable=invalid-name
        return super().save(*args, **kwargs)

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'organization'
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ('name', )

@receiver(pre_save, sender=Organization)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    """
    Set parameter values to html friendly format
    """
    instance.id = slugify(instance.name)
