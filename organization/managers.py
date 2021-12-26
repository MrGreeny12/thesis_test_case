from django.db import models
from django.db.models import QuerySet


class EmployeeManager(models.Manager):

    def get_salary_sum(self, department) -> int:
        employees = self.all().filter(department=department)
        salary_sum = int()
        for employee in employees:
            salary_sum += employee.salary

        return salary_sum

    def get_employee_count(self, department) -> int:
        return self.all().filter(department=department).count()
