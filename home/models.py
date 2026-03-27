# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Courier(models.Model):

    #__Courier_FIELDS__
    telegram_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    is_allowed = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Courier_FIELDS__END

    class Meta:
        verbose_name        = _("Courier")
        verbose_name_plural = _("Courier")


class District(models.Model):

    #__District_FIELDS__
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__District_FIELDS__END

    class Meta:
        verbose_name        = _("District")
        verbose_name_plural = _("District")


class City(models.Model):

    #__City_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__City_FIELDS__END

    class Meta:
        verbose_name        = _("City")
        verbose_name_plural = _("City")


class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Packaging(models.Model):

    #__Packaging_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Packaging_FIELDS__END

    class Meta:
        verbose_name        = _("Packaging")
        verbose_name_plural = _("Packaging")


class Productvariant(models.Model):

    #__Productvariant_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)

    #__Productvariant_FIELDS__END

    class Meta:
        verbose_name        = _("Productvariant")
        verbose_name_plural = _("Productvariant")


class Courierassignment(models.Model):

    #__Courierassignment_FIELDS__
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()
    is_hidden = models.BooleanField()
    sent_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    closed_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Courierassignment_FIELDS__END

    class Meta:
        verbose_name        = _("Courierassignment")
        verbose_name_plural = _("Courierassignment")


class Courierassignmentitem(models.Model):

    #__Courierassignmentitem_FIELDS__
    assignment = models.ForeignKey(CourierAssignment, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    planned_qty = models.IntegerField(null=True, blank=True)

    #__Courierassignmentitem_FIELDS__END

    class Meta:
        verbose_name        = _("Courierassignmentitem")
        verbose_name_plural = _("Courierassignmentitem")



#__MODELS__END
