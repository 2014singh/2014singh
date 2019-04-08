from django.db import models

class EmpData(models.Model):
    emp_id=models.IntegerField()
    emp_first_name=models.CharField(max_length=50)
    emp_last_name=models.CharField(max_length=50)
    emp_mobile_number=models.BigIntegerField()
    emp_email_id=models.EmailField(max_length=50)
    emp_salary=models.IntegerField()
    emp_location=models.CharField(max_length=100)
    emp_position=models.CharField(max_length=100)


