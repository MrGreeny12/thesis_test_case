from rest_framework import generics, permissions, views
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from rest_framework.response import Response

from organization.filters import EmployeesFilter
from organization.models import Employee, Department
from organization.serializers import EmployeeSerializer


class EmployeesListAPIView(generics.ListCreateAPIView):
    '''
    API точка для получения списка пользователей и создания новых пользователей
    '''
    queryset = Employee.active.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmployeesFilter


class EmployeeAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''
    API точка для просмотра, редактирования и удаления сотрудников
    '''
    queryset = Employee.active.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class DepartmentsListAPIView(views.APIView):
    '''
    API точка для получения данных о департаментах (список)
    '''

    def get(self, request):
        department_queryset = Department.objects.all()
        departments = list()
        for department in department_queryset:
            department_data = {
                "id": department.pk,
                "name": department.name,
                "salary_sum": Employee.active.get_salary_sum(department=department),
                "employees_count": Employee.active.get_employee_count(department=department)
            }
            departments.append(department_data)

        return Response({
            "departments": departments
        })
