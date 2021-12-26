from django.db import models

from organization.managers import EmployeeManager


def employee_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/employee_<id>/<filename>
    return 'employees/employee_{0}/{1}'.format(instance.id, filename)


class Department(models.Model):
    '''
    Модель департамента
    '''
    name = models.CharField(max_length=512, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Employee(models.Model):
    '''
    Модель сотрудника организации
    '''
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=256, verbose_name='Отчество')
    photo = models.ImageField(upload_to=employee_directory_path, blank=True, null=True, verbose_name='Фото')
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees',
        verbose_name='Департамент'
    )
    post = models.CharField(max_length=256, null=True, blank=True, verbose_name='Должность')
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    salary = models.IntegerField(null=True, blank=True, verbose_name='Зарплата')

    active = EmployeeManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        db_table = 'employee'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        unique_together = ['id', 'department']
        indexes = [
            models.Index(fields=['last_name'])
        ]
