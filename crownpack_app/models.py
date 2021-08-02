from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, first_name, last_name, username, password, department, position, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is _staff= True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is _staff= True.')

        return self.create_user(self, first_name, last_name, username, password, department, 
        position, **other_fields)




    def create_user(self, first_name, last_name, username, password, department, position, **other_fields):

        if not username:
            raise ValueError(_('You must provide a registration no'))
        email = self.normalize_email(email)
        user = self.model(email=email, reg_no=username, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()

        return user
   



class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField('First Name', max_length=64, unique=True)
    other_name = models.CharField('Other Name', max_length=64)
    last_name = models.CharField('Last Name', max_length=64, unique=True)
    email = models.EmailField('Email')
    username = models.TextField('Registration No', unique=True)
    department = models.CharField('Department', max_length=64, unique=True)
    position = models.TextField('Position', unique=True)
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

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['first_name']

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.reg_no}"
