from ctypes import addressof
from distutils.command.upload import upload
from email import message
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER=(
        (1,'superAdmin'),
        (2,'admin'),
        (3,'student'),
    )
    user_type=models.CharField(choices=USER,max_length=100,default=1)
    profile_pic=models.ImageField(upload_to='media/profile_pic')

class Course(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class SessionYear(models.Model):
    session_start=models.CharField(max_length=100)
    session_end=models.CharField(max_length=100)

    def __str__(self):
        return self.session_start +" - "+ self.session_end
    
class Student(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=100)
    course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    sessionyear_id=models.ForeignKey(SessionYear,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name +" "+ self.admin.last_name
    
class Staff(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name +" "+ self.admin.last_name
    
class Subject(models.Model):
    name=models.CharField(max_length=100)
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    staff= models.ForeignKey(Staff,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class staff_notification(models.Model):
    admin_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.admin_id.admin.first_name
    
class staff_leave(models.Model):
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    message= models.TextField()
    status = models.IntegerField(null=True,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name +" "+ self.staff_id.admin.last_name

class student_leave(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    message= models.TextField()
    status = models.IntegerField(null=True,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student_id.admin.first_name +" "+ self.student_id.admin.last_name
    
class student_notification(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.student_id.admin.first_name


class student_result(models.Model):
   student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
   subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
   assignment_marks=models.IntegerField()
   exam_marks=models.IntegerField()
   total=models.IntegerField(default=0)
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)
   
   def __str__(self):
        return self.student_id.admin.first_name
   