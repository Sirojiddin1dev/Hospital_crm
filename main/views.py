from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

"""START EMPLOYEE FILTER API"""


@api_view(['GET'])
def filter_employee_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    employee = Employee.objects.filter(phone_number=phone_number)
    ser = EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_name(request):
    name = request.GET.get('name')
    employee = Employee.objects.filter(name=name)
    ser = EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_lavozim(request):
    lavozim = request.GET.get('lavozim')
    employee = Employee.objects.filter(lavozim=lavozim)
    ser = EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_department(request):
    department = request.GET.get('department')
    employee = Employee.objects.filter(department=department)
    ser = EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_room(request):
    room = request.GET.get('room')
    employee = Employee.objects.filter(room=room)
    ser = EmployeeSerializer(employee)
    return Response(ser.data)


"""END EMPLOYEE FILTER API"""


"""START EQUIPMENT FILTER API"""

@api_view(['GET'])
def filter_equipment_by_type(request):
    type = request.GET.get('type')
    equipment = Equipment.objects.filter(type=type)
    ser = EquipmentSerializer(equipment)
    return Response(ser.data)


@api_view(['GET'])
def filter_equipment_by_name(request):
    name = request.GET.get('name')
    equipment = Equipment.objects.filter(name=name)
    ser = EquipmentSerializer(equipment)
    return Response(ser.data)


@api_view(['GET'])
def filter_equipment_by_room(request):
    room = request.GET.get('room')
    equipment = Equipment.objects.filter(room=room)
    ser = EquipmentSerializer(equipment)
    return Response(ser.data)


"""END EQUIPMENT FILTER API"""


"""START PATIENT FILTER API"""


@api_view(['GET'])
def filter_patient_by_name(request):
    name = request.GET.get('name')
    patient = Patient.objects.filter(name=name)
    ser = PatientSerializer(patient)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    patient = Patient.objects.filter(phone_number=phone_number)
    ser = PatientSerializer(patient)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_illness(request):
    illness = request.GET.get('illness')
    patient = Patient.objects.filter(illness=illness)
    ser = PatientSerializer(patient)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_doctor(request):
    doctor = request.GET.get('doctor')
    patient = Patient.objects.filter(doctor=doctor)
    ser = PatientSerializer(patient)
    return Response(ser.data)


"""END PATIENT FILTER API"""


"""START PAYMENT FILTER API """


@api_view(['GET'])
def filter_payment_by_date(request):
    date = request.GET.get('date')
    payment = Payment.objects.filter(date=date)
    ser = PaymentSerializer(payment)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_by_type(request):
    type = request.GET.get('type')
    payment = Payment.objects.filter(type=type)
    ser = PaymentSerializer(payment)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_by_patient(request):
    patient = request.GET.get('patient')
    payment = Payment.objects.filter(patient=patient)
    ser = PaymentSerializer(payment)
    return Response(ser.data)


"""END PAYMENT FILTER API"""


"""START DEPARTMENT FILTER API"""


@api_view(['GET'])
def filter_department_by_name(request):
    name = request.GET.get('name')
    department = Department.objects.filter(name=name)
    ser = DepartmentSerializer(department)
    return Response(ser.data)


"""END DEPARTMENT FILTER API"""


"""START OPERATION FILTER API"""


@api_view(['GET'])
def filter_operation_by_patient(request):
    patient = request.GET.get('patient')
    operation = Operation.objects.filter(patient=patient)
    ser = OperationSerializer(operation)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_name(request):
    name = request.GET.get('name')
    operation = Operation.objects.filter(name=name)
    ser = OperationSerializer(operation)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_date(request):
    date = request.GET.get('date')
    operation = Operation.objects.filter(date=date)
    ser = OperationSerializer(operation)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_employee(request):
    employee = request.GET.get('employee')
    operation = Operation.objects.filter(emloyee=employee)
    ser = OperationSerializer(operation)
    return Response(ser.data)
"""END OPERATION FILTER API"""
