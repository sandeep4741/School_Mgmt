from django.db import models
# Create your models here.


class Student_Data(models.Model):
    Student_Name = models.CharField(max_length=30)
    Class = models.IntegerField()
    RollNumber = models.IntegerField(primary_key=True)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=10)
    Address = models.CharField(max_length=30)


class Teacher_Data(models.Model):
    Name = models.CharField(max_length=30)
    TeacherId = models.IntegerField(primary_key=True)
    Qualification = models.CharField(max_length=30)
    DateOfJoining = models.DateField()
    Gender = models.CharField(max_length=10)
    Subject = models.CharField(max_length=30)


class Student_Performance(models.Model):
    Student_Name = models.CharField(max_length=30)
    Class = models.IntegerField()
    RollNumber = models.IntegerField(primary_key=True)
    Grade = models.CharField(max_length=10)
    Remarks = models.CharField(max_length=20)


class Teacher_Performance(models.Model):
    Teacher_Name = models.CharField(max_length=30)
    TeacherId = models.IntegerField()
    Subject = models.CharField(max_length=30)
    Remarks = models.CharField(max_length=20)
