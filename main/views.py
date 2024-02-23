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
    employee = EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_name(request):
    name = request.GET.get('name')
    employee = Employee.objects.filter(name=name)
    employee = EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_lavozim(request):
    lavozim = request.GET.get('lavozim')
    employee = Employee.objects.filter(lavozim=lavozim)
    employee = EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_department(request):
    department = request.GET.get('department')
    employee = Employee.objects.filter(department=department)
    employee = EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_room(request):
    room = request.GET.get('room')
    employee = Employee.objects.filter(room=room)
    employee = EmployeeSerializer(employee)
    return Response(ser.data)


"""END EMPLOYEE FILTER API"""


"""START EQUIPMENT FILTER API"""

@api_view(['GET'])
def filter_equipment_by_type(request):
    type = request.GET.get('type')
    equipment = Equipment.objects.filter(type=type)
    equipment = EquipmentSerializer(equipment)
    return Response(ser.data)


@api_view(['GET'])
def filter_equipment_by_name(request):
    name = request.GET.get('name')
    equipment = Equipment.objects.filter(name=name)
    equipment = EquipmentSerializer(equipment)
    return Response(ser.data)


@api_view(['GET'])
def filter_equipment_by_room(request):
    room = request.GET.get('room')
    equipment = Equipment.objects.filter(room=room)
    equipment = EquipmentSerializer(equipment)
    return Response(ser.data)


"""END EQUIPMENT FILTER API"""


"""START PATIENT FILTER API"""


@api_view(['GET'])
def filter_patient_by_name(request):
    name = request.GET.get('name')
    patient = Patient.objects.filter(name=name)
    patient = PatientSerializer(patient)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    patient = Patient.objects.filter(phone_number=phone_number)
    patient = PatientSerializer(patient)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_illness(request):
    illness = request.GET.get('illness')
    patient = Patient.objects.filter(illness=illness)
    patient = PatientSerializer(patient)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_doctor(request):
    doctor = request.GET.get('doctor')
    patient = Patient.objects.filter(doctor=doctor)
    patient = PatientSerializer(patient)
    return Response(ser.data)


"""END PATIENT FILTER API"""


"""START PAYMENT FILTER API """


@api_view(['GET'])
def filter_payment_by_date(request):
    date = request.GET.get('date')
    payment = Payment.objects.filter(date=date)
    payment = PaymentSerializer(payment)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_by_type(request):
    type = request.GET.get('type')
    payment = Payment.objects.filter(type=type)
    payment = PaymentSerializer(payment)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_by_patient(request):
    patient = request.GET.get('patient')
    payment = Payment.objects.filter(patient=patient)
    payment = PaymentSerializer(payment)
    return Response(ser.data)


"""END PAYMENT FILTER API"""


"""START DEPARTMENT FILTER API"""


@api_view(['GET'])
def filter_department_by_name(request):
    name = request.GET.get('name')
    department = Department.objects.filter(name=name)
    department = DepartmentSerializer(department)
    return Response(ser.data)


"""END DEPARTMENT FILTER API"""


"""START OPERATION FILTER API"""


@api_view(['GET'])
def filter_operation_by_patient(request):
    patient = request.GET.get('patient')
    operation = Operation.objects.filter(patient=patient)
    operation = OperationSerializer(operation)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_name(request):
    name = request.GET.get('name')
    operation = Operation.objects.filter(name=name)
    operation = OperationSerializer(operation)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_date(request):
    date = request.GET.get('date')
    operation = Operation.objects.filter(date=date)
    operation = OperationSerializer(operation)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_employee(request):
    employee = request.GET.get('employee')
    operation = Operation.objects.filter(emloyee=employee)
    operation = OperationSerializer(operation)
    return Response(ser.data)


"""END OPERATION FILTER API"""