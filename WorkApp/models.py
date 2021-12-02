from django.contrib.auth.models import User
from django.db import models
from WorkApp import validators as custom_validators
from WorkApp.constants import *
from mptt.models import MPTTModel, TreeForeignKey


class Names(models.Model):
    first_name = models.CharField(max_length=FIRST_NAME_LEN)
    second_name = models.CharField(max_length=SECOND_NAME_LEN)
    third_name = models.CharField(max_length=THIRD_NAME_LEN)


class DateWork(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)


class Client(DateWork):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    id = models.CharField(max_length=ID_LEN,
                          validators=[custom_validators.validate_correct_client_id])
    phone = models.CharField(max_length=PHONE_LEN,
                             unique=True)
    name = models.ForeignKey(Names,
                             on_delete=models.DO_NOTHING)

    status = models.BooleanField(default=True)
    client_type = models.CharField(choices=CLIENT_TYPES,
                                   max_length=CLIENT_TYPE_LEN)
    gender = models.CharField(choices=GENDER,
                              max_length=GENDER_LEN)
    timezone = models.CharField(choices=TIMEZONES,
                                max_length=TIMEZONE_LEN)


class PhoneNumbers(models.Model):
    """
        Справочник с доп. телефонами клиента
    """
    owner = models.ForeignKey(Client,
                              on_delete=models.CASCADE,)
    phone = models.CharField(max_length=PHONE_LEN)


class Emails(models.Model):
    """
        Справочник с доп. телефонами клиента
    """
    owner = models.ForeignKey(Client,
                              on_delete=models.CASCADE,)
    email = models.EmailField()


class SocialNetworks(models.Model):
    owner = models.ForeignKey(Client,
                              on_delete=models.CASCADE, )
    social_name = models.CharField(max_length=SOCIAL_NAME_LEN)
    social_id = models.CharField(max_length=SOCIAL_ID_LEN)


class LegalPerson(DateWork):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    id = models.CharField(max_length=ID_LEN,
                          validators=[custom_validators.validate_correct_legal_person_id])
    full_title = models.CharField(max_length=FULL_TITLE_LEN)
    short_title = models.CharField(max_length=SHORT_TITLE_LEN)
    INN = models.IntegerField()
    KPP = models.IntegerField()


class Departments(MPTTModel):
    id = models.CharField(max_length=ID_LEN,
                          validators=[custom_validators.validate_correct_department],
                          primary_key=True)
    title = models.CharField(max_length=DEPARTMENT_TITLE_LEN)
    parent_department = TreeForeignKey('self',
                                       blank=True,
                                       null=True,
                                       help_text='родитель нового департамента',
                                       on_delete=models.CASCADE)
