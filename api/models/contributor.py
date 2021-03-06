# -*- coding: utf-8 -*-
"""
Defines the Contributor model
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .base import Base

# Create your models here.
class Contributor(Base):
    """
    Definition for Contributor
    """
    # Relationships

    # Attributes

    # Manager

    # Functions
    # def __str__(self):
    #     """
    #     __str__
    #     """
    #     return self.name

    # def __unicode__(self):
    #     """
    #     __unicode__
    #     """
    #     return self.name

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'contributor'
        verbose_name = 'Contributor'
        verbose_name_plural = 'Contributors'
        ordering = ['name']

@receiver(pre_save, sender=Contributor)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    '''
    Set parameter values to html friendly format
    '''
    instance.id = slugify(instance.name)
