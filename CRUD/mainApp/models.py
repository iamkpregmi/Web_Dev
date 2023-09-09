from django.db import models

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=20)
    Salary = models.IntegerField()