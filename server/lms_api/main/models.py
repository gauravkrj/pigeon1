from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100,default='booran')
    mobile_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    #classroom = models.ForeignKey(on_delete=models.SET_NULL, null=True)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100,default='booran')
    roll_number = models.IntegerField(max_length=10,default=0)
    mobile_number = models.CharField(max_length=10)
   # classroom = models.ForeignKey(on_delete=models.SET_NULL, null=True)
    #parent = models.ForeignKey(Parent ,on_delete=models.CASCADE null=True, blank=True)


class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100,default='booran')
    mobile_number = models.CharField(max_length=10)



class Classroom(models.Model):
    name = models.CharField(max_length=100)
    #class_teacher = models.ForeignKey(on_delete=models.SET_NULL, null=True)


class Adminstaff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100,default='booran')
    mobile_number = models.CharField(max_length=10)
    



# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class Usermanager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class Useraccount(AbstractBaseUser):
#     USER_TYPES = (
#         ('adminstaff', 'Admin Staff'),
#         ('teacher', 'Teacher'),
#         ('student', 'Student'),
#         ('parent', 'Parent'),
#        # ('classroom', 'Classroom'),
#     )

#     email = models.EmailField(unique=True)
#     user_type = models.CharField(choices=USER_TYPES, max_length=20)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     # Name aur date of birth jaise aur common user fields ko bhi add karein

#     objects = Usermanager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_type']

#     def __str__(self):
#         return self.email
# # Create your models here.
