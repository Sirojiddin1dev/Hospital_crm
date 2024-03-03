from django.urls import path
from .views import *

urlpatterns = [
    # Employee Filter URLs
    path('filter/employee/by-phone-number/', filter_employee_by_phone_number),
    path('filter/employee/by-name/', filter_employee_by_name),
    path('filter/employee/by-lavozim/', filter_employee_by_lavozim),
    path('filter/employee/by-department/', filter_employee_by_department),
    path('filter/employee/by-room/', filter_employee_by_room),
    path('filter/employee/by-salary/', filter_employee_by_salary),

    # Equipment Filter URLs
    path('filter/equipment/by-type/', filter_equipment_by_type),
    path('filter/equipment/by-name/', filter_equipment_by_name),

    # Patient Filter URLs
    path('filter/patient/by-name/', filter_patient_by_name),
    path('filter/patient/by-phone-number/', filter_patient_by_phone_number),
    path('filter/patient/by-illness/', filter_patient_by_illness),
    path('filter/patient/by-doctor/', filter_patient_by_doctor),
    path('filter/patient/by-gender/', filter_patient_by_gender),

    # Payment Filter URLs
    path('filter/payment/by-date/', filter_payment_by_date),
    path('filter/payment/by-type/', filter_payment_by_type),
    path('filter/payment/by-patient/', filter_payment_by_patient),

    # Department Filter URLs
    path('filter/department/by-name/', filter_department_by_name),

    # Operation Filter URLs
    path('filter/operation/by-patient/', filter_operation_by_patient),
    path('filter/operation/by-name/', filter_operation_by_name),
    path('filter/operation/by-date/', filter_operation_by_date),
    path('filter/operation/by-employee/', filter_operation_by_employee),

    # Room Filter URLs
    path('filter/room/by-name/', filter_room_by_name),
    path('filter/room/by-status/', filter_room_by_status),
    path('filter/room/by-capacity/', filter_room_by_capacity),
    path('filter/room/by-booked/', filter_room_by_booked),
    path('filter/room/by-equipment/', filter_room_by_equipment),
    path('filter/room/by-department/', filter_room_by_department),

    # Testimonial Filter URLs
    path('filter/testimonial/by-rate/', filter_testimonial_by_rate),

    # Kassa Filter URLs
    path('filter/kassa/by-amount/', filter_kassa_by_amount),
    path('filter/kassa/by-date/', filter_kassa_by_date),

    # Attendance Filter URLs
    path('filter/attendance/by-date/', filter_attendance_by_date),
    path('filter/attendance/by-employee/', filter_attendance_by_employee),
]
