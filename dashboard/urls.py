from django.urls import path
from .views import *


urlpatterns = [
    # Employee URLs
    path('employees/', EmployeeListAPIView.as_view()),
    path('employees/create/', EmployeeListCreateAPIView.as_view()),
    path('employees/<int:pk>/update/', EmployeeUpdateAPIView.as_view()),
    path('employees/<int:pk>/delete/', EmployeeDestroyAPIView.as_view()),

    # Circulation URLs
    path('circulations/', CirculationListAPIView.as_view()),
    path('circulations/create/', CirculationListCreateAPIView.as_view()),
    path('circulations/<int:pk>/update/', CirculationUpdateAPIView.as_view()),
    path('circulations/<int:pk>/delete/', CirculationDestroyAPIView.as_view()),

    # Room URLs
    path('rooms/', RoomListAPIView.as_view()),
    path('rooms/create/', RoomListCreateAPIView.as_view()),
    path('rooms/<int:pk>/update/', RoomUpdateAPIView.as_view()),
    path('rooms/<int:pk>/delete/', RoomDestroyAPIView.as_view()),

    # Payment URLs
    path('payments/', PaymentListAPIView.as_view()),
    path('payments/create/', PaymentListCreateAPIView.as_view()),
    path('payments/<int:pk>/update/', PaymentUpdateAPIView.as_view()),
    path('payments/<int:pk>/delete/', PaymentDestroyAPIView.as_view()),

    # Department URLs
    path('departments/', DepartmentListAPIView.as_view()),
    path('departments/create/', DepartmentListCreateAPIView.as_view()),
    path('departments/<int:pk>/update/', DepartmentUpdateAPIView.as_view()),
    path('departments/<int:pk>/delete/', DepartmentDestroyAPIView.as_view()),

    # ClinicStatistic URLs
    path('clinicstatistics/', ClinicStatisticListAPIView.as_view()),
    path('clinicstatistics/create/', ClinicStatisticListCreateAPIView.as_view()),
    path('clinicstatistics/<int:pk>/update/', ClinicStatisticUpdateAPIView.as_view()),
    path('clinicstatistics/<int:pk>/delete/', ClinicStatisticDestroyAPIView.as_view()),

    # Patient URLs
    path('patients/', PatientListAPIView.as_view()),
    path('patients/create/', PatientListCreateAPIView.as_view()),
    path('patients/<int:pk>/update/', PatientUpdateAPIView.as_view()),
    path('patients/<int:pk>/delete/', PatientDestroyAPIView.as_view()),

    # Testimonial URLs
    path('testimonials/', TestimonialListAPIView.as_view()),
    path('testimonials/create/', TestimonialListCreateAPIView.as_view()),
    path('testimonials/<int:pk>/update/', TestimonialUpdateAPIView.as_view()),
    path('testimonials/<int:pk>/delete/', TestimonialDestroyAPIView.as_view()),

    # Equipment URLs
    path('equipment/', EquipmentListAPIView.as_view()),
    path('equipment/create/', EquipmentListCreateAPIView.as_view()),
    path('equipment/<int:pk>/update/', EquipmentUpdateAPIView.as_view()),
    path('equipment/<int:pk>/delete/', EquipmentDestroyAPIView.as_view()),

    # Operation URLs
    path('operations/', OperationListAPIView.as_view()),
    path('operations/create/', OperationListCreateAPIView.as_view()),
    path('operations/<int:pk>/update/', OperationUpdateAPIView.as_view()),
    path('operations/<int:pk>/delete/', OperationDestroyAPIView.as_view()),

    # Attendance URLs
    path('attendance/', AttendanceListAPIView.as_view()),
    path('attendance/create/', AttendanceListCreateAPIView.as_view()),
    path('attendance/<int:pk>/update/', AttendanceUpdateAPIView.as_view()),
    path('attendance/<int:pk>/delete/', AttendanceDestroyAPIView.as_view()),
]
