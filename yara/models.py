from django.contrib.auth.models import User
from django.db import models
from django_extensions.db import fields
from yara.managers import StateManager

#TODO Upate how we get the User model


class Base(models.Model):
    created = fields.CreationDateTimeField()
    created_by = models.ForeignKey(User, null=True, blank=True)
    updated = fields.ModificationDateTimeField()
    updated_by = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        abstract = True


class State(Base):
    code = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(unique=True, max_length=100)
    objects = StateManager()

    class Meta:
        verbose_name = "state"
        verbose_name_plural = "states"
        ordering = ["name"]

    def __repr__(self):
        return self.name


class Phone(Base):
    area_code = models.CharField(max_length=3)
    exchange = models.CharField(max_length=3)
    number = models.CharField(max_length=4)

    class Meta:
        verbose_name = "phone"
        verbose_name_plural = "phones"
        unique_together = ("area_code", "exchange", "number")

    def __repr__(self):
        return "(%s) %s-%s" % (self.area_code, self.exchange, self.number,)


class Address(Base):
    street1 = models.CharField(max_length=150)
    street2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State)
    postal_code = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'

    def __repr__(self):
        return '%s %s, %s %s' % (self.street1, self.city, self.state.code, self.postal_code)


class UserProfile(Base):
    pass