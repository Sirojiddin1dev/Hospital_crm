from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
import qrcode
from io import BytesIO
from django.core.files import File


class User(AbstractUser):
    age = models.IntegerField(verbose_name='Yosh')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    LAVOZIM_CHOICES = (
        ('Nurse', 'Nurse'),
        ('Doctor', 'Doctor'),
        ('Manager', 'Manager'),
        ('Admin', 'Admin'),
    )
    lavozimi = models.CharField(max_length=55, verbose_name='lavozim', choices=LAVOZIM_CHOICES)
    birth_date = models.DateField(verbose_name='Your birthday')
    phone_number = models.CharField(max_length=13, null=True, blank=True, verbose_name='Phone_Number', validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    email = models.EmailField()
    RegexValidator(
        regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message='Invalide email',
        code='Invalid email'
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Famale', 'Famale')
    )
    gender = models.CharField(max_length=55, verbose_name='Gender', choices=GENDER_CHOICES)
    room = models.ForeignKey(to='Rooms', verbose_name='Room',  on_delete=models.PROTECT)
    salary = models.BigIntegerField(verbose_name='Salary')
