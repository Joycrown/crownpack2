from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField('First Name', max_length=64)
    other_name = models.CharField('Other Name', max_length=64)
    last_name = models.CharField('Last Name', max_length=64)
    email = models.EmailField('Email', unique=True)
    reg_no = models.TextField('Registration No', unique=True)
    department = models.CharField('Department', max_length=64)
    position = models.TextField('Position')
    dob = models.DateField('Date Of Birth')
    sex = models.CharField('Sex', choices=[
        ('M','Male'),
        ('F','Female'),
        ('O','Prefer Not to Say')
    ], max_length=1)
    phone_no = models.CharField('Phone No', max_length=11)
    address = models.TextField('Address')
    next_of_kin = models.CharField('Next Of Kin', max_length=64)
    phone_no_nok = models.CharField('Phone No Of Next Of Kin', max_length=11)


    USERNAME_FIELD = 'reg_no'

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.reg_no}"
