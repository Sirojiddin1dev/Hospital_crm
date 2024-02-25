from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

"""START EMPLOYEE FILTER API"""


@api_view(['GET'])
def filter_employee_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    employee = Employee.objects.filter(phone_number=phone_number)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_name(request):
    name = request.GET.get('name')
    employee = Employee.objects.filter(name=name)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_lavozim(request):
    lavozim = request.GET.get('lavozim')
    employee = Employee.objects.filter(lavozim=lavozim)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_department(request):
    department = request.GET.get('department')
    employee = Employee.objects.filter(department=department)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_room(request):
    room = request.GET.get('room')
    employee = Employee.objects.filter(room=room)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_salary(request):
    salary = request.GET.get('salary')
    employee = Employee.objects.filter(salary=salary)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


"""END EMPLOYEE FILTER API"""

"""START EQUIPMENT FILTER API"""


@api_view(['GET'])
def filter_equipment_by_type(request):
    type = request.GET.get('type')
    equipment = Equipment.objects.filter(type=type)
    ser = EquipmentSerializer(equipment, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_equipment_by_name(request):
    name = request.GET.get('name')
    equipment = Equipment.objects.filter(name__icontains=name)
    ser = EquipmentSerializer(equipment, many=True)
    return Response(ser.data)


"""END EQUIPMENT FILTER API"""

"""START PATIENT FILTER API"""


@api_view(['GET'])
def filter_patient_by_name(request):
    name = request.GET.get('name')
    patient = Patient.objects.filter(name__icontains=name)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    patient = Patient.objects.filter(phone_number=phone_number)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_illness(request):
    illness = request.GET.get('illness')
    patient = Patient.objects.filter(illness=illness)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_doctor(request):
    doctor = request.GET.get('doctor')
    patient = Patient.objects.filter(doctor=doctor)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_gender(request):
    gender = request.GET.get('gender')
    patient = Patient.objects.filter(gender=gender)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


"""END PATIENT FILTER API"""


"""START PAYMENT FILTER API """


@api_view(['GET'])
def filter_payment_by_date(request):
    date = request.GET.get('date')
    payment = Payment.objects.filter(date=date)
    ser = PaymentSerializer(payment, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_by_type(request):
    type = request.GET.get('type')
    payment = Payment.objects.filter(type=type)
    ser = PaymentSerializer(payment, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_by_patient(request):
    patient = request.GET.get('patient')
    payment = Payment.objects.filter(patient=patient)
    ser = PaymentSerializer(payment, many=True)
    return Response(ser.data)


"""END PAYMENT FILTER API"""


"""START DEPARTMENT FILTER API"""


@api_view(['GET'])
def filter_department_by_name(request):
    name = request.GET.get('name')
    department = Department.objects.filter(name=name)
    ser = DepartmentSerializer(department, many=True)
    return Response(ser.data)


"""END DEPARTMENT FILTER API"""


"""START OPERATION FILTER API"""


@api_view(['GET'])
def filter_operation_by_patient(request):
    patient = request.GET.get('patient')
    operation = Operation.objects.filter(patient=patient)
    ser = OperationSerializer(operation, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_name(request):
    name = request.GET.get('name')
    operation = Operation.objects.filter(name__icontains=name)
    ser = OperationSerializer(operation, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_date(request):
    date = request.GET.get('date')
    operation = Operation.objects.filter(date=date)
    ser = OperationSerializer(operation, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_employee(request):
    employee = request.GET.get('employee')
    operation = Operation.objects.filter(emloyee=employee)
    ser = OperationSerializer(operation, many=True)
    return Response(ser.data)


"""END OPERATION FILTER API"""

"""Start Room Filter API"""


@api_view(['GET'])
def filter_room_by_name(request):
    name = request.GET.get('name')
    room = Room.objects.filter(name=name)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_by_status(request):
    status = request.GET.get('status')
    room = Room.objects.filter(status=status)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_by_capacity(request):
    capacity = request.GET.get('capacity')
    room = Room.objects.filter(capacity=capacity)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_by_capacity(request):
    capacity = request.GET.get('capacity')
    room = Room.objects.filter(capacity=capacity)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_by_equipment(request):
    equipment = request.GET.get('equipment')
    room = Room.objects.filter(equipment=equipment)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_by_department(request):
    department = request.GET.get('department')
    room = Room.objects.filter(department=department)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


"""END ROOM FILTER API"""

"""START TESTIMONIAL FILTER API"""


@api_view(['GET'])
def filter_testimonial_by_rate(request):
    rate = request.GET.get('rate')
    testimonial = Testimonial.objects.filter(rate=rate)
    ser = TestimonialSerializer(testimonial, many=True)
    return Response(ser.data)


"""END TESTIMONIAL FILTER API"""

"""START KASSA FILTER API"""


@api_view(['GET'])
def filter_kassa_by_amount(request):
    amount = request.GET.get('amount')
    kassa = Kassa.objects.filter(amount=amount)
    ser = KassaSerializer(kassa, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_kassa_by_date(request):
    date = request.GET.get('date')
    kassa = Kassa.objects.filter(date=date)
    ser = KassaSerializer(kassa, many=True)
    return Response(ser.data)


"""END KASSA FILTER API"""

"""START ATTENDANCE FILTER API"""


@api_view(['GET'])
def filter_attendance_by_date(request):
    date = request.GET.get('date')
    attendance = Attendance.objects.filter(date=date)
    ser = AttendanceSerializer(attendance, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_attendance_by_employee(request):
    employee = request.GET.get('employee')
    attendance = Attendance.objects.filter(employee=employee)
    ser = AttendanceSerializer(attendance, many=True)
    return Response(ser.data)


"""END ATTENDANCE FILTER API"""
