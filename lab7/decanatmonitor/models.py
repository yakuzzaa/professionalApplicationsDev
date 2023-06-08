from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100)


class StudentGroup(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)


class Spravka(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField()
    scholarship = models.ForeignKey('Scholarship', on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)


class Scholarship(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
