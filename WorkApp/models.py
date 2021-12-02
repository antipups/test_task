from django.contrib.auth.models import User
from django.db import models
from WorkApp import validators as custom_validators
from WorkApp.constants import *


class Names(models.Model):
    first_name = models.CharField(max_length=FIRST_NAME_LEN)
    second_name = models.CharField(max_length=SECOND_NAME_LEN)
    third_name = models.CharField(max_length=THIRD_NAME_LEN)

    def __str__(self):
        return self.second_name + ' ' + self.first_name + ' ' + self.third_name


class DateWork(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True, auto_now=True)


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

    def __str__(self):
        return str(self.id) + ' ' + self.name.second_name


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
    class Meta:
        abstract = True

    owner = models.ForeignKey(Client,
                              on_delete=models.CASCADE, )
    social_name = models.CharField(max_length=SOCIAL_NAME_LEN)
    social_id = models.CharField(max_length=SOCIAL_ID_LEN)


class SocialNetworksUniq(SocialNetworks):
    class Meta:
        unique_together = ('owner', 'social_name',)

    social_name = models.CharField(max_length=SOCIAL_NAME_LEN,
                                   choices=UNIQ_SOCIALS)


class SocialNetworksNotUniq(SocialNetworksUniq):
    social_name_not_uniq = models.CharField(max_length=SOCIAL_NAME_LEN,
                                            choices=NOT_UNIQ_SOCIALS,
                                            verbose_name='social_name')


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

    def __str__(self):
        return self.short_title


class Departments(models.Model):
    id = models.CharField(max_length=ID_LEN,
                          validators=[custom_validators.validate_correct_department],
                          primary_key=True)
    title = models.CharField(max_length=DEPARTMENT_TITLE_LEN)
    parent_department = models.ForeignKey('self',
                                          blank=True,
                                          null=True,
                                          related_name='children',
                                          help_text='родитель нового департамента',
                                          on_delete=models.CASCADE)
    owners = models.ManyToManyField(LegalPerson)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return str(self.clients.count())
