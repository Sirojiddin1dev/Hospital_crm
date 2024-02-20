from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
import qrcode
from io import BytesIO
from django.core.files import File


class User(AbstractUser):
    age = models.IntegerField(verbose_name='Yosh', null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True, verbose_name='Telefon raqam', validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    LAVOZIM_CHOICES = (
        ('Nurse', 'Nurse'),
        ('Doctor', 'Doctor'),
        ('Manager', 'Manager')
        ('Admin', 'Admin')
    )
    lavozimi = models.CharField(max_length=55, verbose_name='lavozim', choices=LAVOZIM_CHOICES)
    birth_date = models.DateField(verbose_name = 'Your birthday')
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
    gender = models.CharField(max_length=55,verbose_name='Gender', choices=GENDER_CHOICES)
    room = models.ForeignKey(to='Room', verbose_name = 'Room',  on_delete=models.PROTECT)
    salary = models.BigIntegerField(verbose_name = 'Salary')
    mutahasisligi = models.ForeignKey(to='Specialty', verbose_name='Mutahasisligi', on_delete=models.CASCADE)
    department = models.ForeignKey(to='Department', verbose_name='Department', on_delete=models.CASCADE)
    user = models.ForeignKey(to='User', verbose_name='User', on_delete=models.CASCADE)

    class Meta(Employee.Meta):
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField(max_length=255, verbose_name='Specialty name')

    class Meta(Specialty.Meta):
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialtys'

    def __str__(self):
        return self.name


class Circulation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Amount")
    date = models.DateField(null=True, verbose_name="Date")
    employee = models.ForeignKey(to='Employee', null=True, on_delete=models.CASCADE, verbose_name="Employee")
    details = models.CharField(max_length=255, verbose_name="Details")

    class Meta(Circulation.Meta):
        verbose_name = 'Circulation'
        verbose_name_plural = 'Circulations'


class Room(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Room Name")
    STATUS_CHOICES =(
        ('Ekonom', 'Ekonom')
        ('Lux', 'Lux')
    )
    status = models.CharField(max_length=20, null=True, verbose_name="Status",choices=STATUS_CHOICES)
    capacity = models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Capacity")
    type = models.CharField(max_length=255, verbose_name="Type")
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE, verbose_name="Department")
    equipment = models.ManyToManyField(to='Equipment', verbose_name="Equipment")

    class Meta(Rooms.Meta):
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.name


class Kassa(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Amount")
    date = models.DateTimeField(verbose_name='Time')


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Amount")
    date = models.DateField(null=True, verbose_name="Date")
    TYPE_CHOICES =(
        ('Click', 'Click')
        ('Cash', 'Cash')
    )
    type = models.CharField(max_length=20, verbose_name="type",choices=TYPE_CHOICES)
    patient = models.ForeignKey(to='Patient', null=True, on_delete=models.CASCADE, verbose_name="Patient")
    STATUS_CHOICES = (
        ('full pay', 'full pay')
        ('average pay', 'average pay')
        ('unpaid', 'unpaid')
    )
    status = models.CharField(max_length=20, verbose_name="status", choices=STATUS_CHOICES)

    class Meta(Payment.Meta):
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)

    class Meta(Department.Meta):
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class ClinicStatistic(models.Model):
    name = models.CharField(max_length=255, verbose_name='Clinic Name')
    patients = models.ManyToManyField(to='Patients', verbose_name="Patients")
    operation = models.ManyToManyField(to='Operation', verbose_name="Operations")
    room = models.ManyToManyField(to='Room', verbose_name="Rooms")
    employee = models.ManyToManyField(to='Employee', verbose_name="Employee")
    date = models.DateField(auto_now=True)

    class Meta(ClinicStatistic.Meta):
        verbose_name = 'ClinicStatistic'
        verbose_name_plural = 'ClinicStatistics'

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=25, verbose_name="Name")
    birth_date = models.DateField(verbose_name="Birth date")
    phone_number = models.CharField(max_length=13, null=True, blank=True, verbose_name='Phone_Number', validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    illnes = models.CharField(max_length=255, verbose_name='Illnes')
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Famale', 'Famale')
    )
    gender = models.CharField(max_length=55,verbose_name='Gender', choices=GENDER_CHOICES)
    doctor = models.ForeignKey(to='Employee', verbose_name="Doctor", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta(Patients.Meta):
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    patient = models.ForeignKey(to='Patient', verbose_name='Patient', on_delete=models.PROTECT)
    RATE_CHOICES = (
        ('Good', 'Good')
        ('Excellent', 'Excellent')
        ('Bad', 'Bad')
    )
    rate = models.CharField(max_length=25, verbose_name="Rate", choices=RATE_CHOICES)
    message = models.CharField(max_length=255, verbose_name='Message', null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta(Testimonial.Meta):
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    type = models.CharField(max_length=255, verbose_name='Type')
    quantity = models.IntegerField(verbose_name='Quantity', default=1)
    created = models.DateField(auto_now=True)

    class Meta(Equipment.Meta):
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'

    def __str__(self):
        return self.name

class Operation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Operation Name')
    patient = models.ForeignKey(to="Patients", verbose_name='Patient', on_delete=models.PROTECT)
    date = models.DateField(verbose_name="Operation date")
    employees = models.ManyToManyField(to='Employee', verbose_name="Doctors")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Operation price")

    class Meta(Operation.Meta):
        verbose_name = 'Operation'
        verbose_name_plural = 'Operations'

    def __str__(self):
        return self.name
