from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Department(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Department Name")

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Equipment Name")
    type = models.CharField(max_length=255, verbose_name="Equipment Type")
    quantity = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Quantity")

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Employee Name")
    position = models.CharField(max_length=50, null=True, verbose_name="Position")
    birth_date = models.DateField(null=True, verbose_name="Date of Birth")
    phone_number = models.CharField(max_length=13, null=True, verbose_name="Phone Number")
    email = models.CharField(max_length=100, null=True, verbose_name="Email")
    gender = models.CharField(max_length=255, verbose_name="Gender")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Department")
    monthly_salary = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Monthly Salary")
    qualification = models.CharField(max_length=255, verbose_name="Qualification")
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="User")

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Patient Name")
    birth_date = models.DateField(null=True, verbose_name="Date of Birth")
    phone_number = models.CharField(max_length=13, null=True, verbose_name="Phone Number")
    illness = models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Illness")
    gender = models.CharField(max_length=255, verbose_name="Gender")
    doctor = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Attending Doctor")

    def __str__(self):
        return self.name


class Surgery(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Surgery Name")
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE, verbose_name="Patient")
    date = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Date")
    surgeon = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Surgeon")
    cost = models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Cost")

    def __str__(self):
        return self.name


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Amount")
    date = models.DateField(null=True, verbose_name="Date")
    type = models.CharField(max_length=50, null=True, verbose_name="Type")
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE, verbose_name="Patient")


class Specialization(models.Model):
    name = models.CharField(max_length=50, verbose_name="Specialization Name")


class FinancialTransaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Amount")
    date = models.DateField(null=True, verbose_name="Date")
    employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, verbose_name="Employee")
    details = models.CharField(max_length=255, verbose_name="Details")


class Room(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Room Name")
    status = models.CharField(max_length=20, null=True, verbose_name="Status")
    capacity = models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Capacity")
    type = models.CharField(max_length=255, verbose_name="Type")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Department")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Equipment")


class ClinicStatistics(models.Model):
    date = models.DateField(null=True, verbose_name="Date")
    patient_count = models.IntegerField(null=True, verbose_name="Patient Count")
    surgery_count = models.IntegerField(null=True, verbose_name="Surgery Count")
    room_count = models.IntegerField(null=True, verbose_name="Room Count")
    patient_count = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE, verbose_name="Patient Count")
    surgery_count = models.ForeignKey(Surgery, null=True, on_delete=models.CASCADE, verbose_name="Surgery Count")
    room_count = models.ForeignKey(Room, null=True, on_delete=models.CASCADE, verbose_name="Room Count")
