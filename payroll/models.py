from django.db import models

# Create your models here.
class Registration_DB(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

class Add_EmployeeDB(models.Model):
    name = models.CharField(max_length=100,default="")
    mobile = models.PositiveBigIntegerField()
    email = models.EmailField()
    addr = models.TextField()
    emp_img = models.ImageField(upload_to="emp_img",default=" ")
    status = models.BooleanField(default=True)

class Add_PayrollDB(models.Model):
    refno = models.CharField(max_length=500,default="")
    datefrom = models.DateField()
    dateto = models.DateField()
    payroll_status = models.CharField(max_length=50,default="Active")
    status = models.BooleanField(default=True)

class Add_AttendanceDB(models.Model):
    date = models.DateField(auto_now=True)
    emp_no = models.PositiveBigIntegerField()
    name = models.CharField(max_length=100,default="")
    time = models.TimeField(auto_now=True)
    status = models.BooleanField(default=True)

class Add_DepartmentDB(models.Model):
    name = models.CharField(max_length=500,default="")
    status = models.BooleanField(default=True)