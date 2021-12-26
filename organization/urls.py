from django.urls import path

from .views import EmployeesListAPIView, EmployeeAPIView, DepartmentsListAPIView


urlpatterns = [
    path('employees/', EmployeesListAPIView.as_view(), name='employee_list_and_employee_create'),
    path('employees/<int:id>/', EmployeeAPIView.as_view(), name='employee'),
    path('departments/', DepartmentsListAPIView.as_view(), name='departments_list')
]
