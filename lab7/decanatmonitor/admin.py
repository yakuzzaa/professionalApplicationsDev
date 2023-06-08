from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Faculty, StudentGroup, Student, Spravka, Scholarship

admin.site.register(Faculty)
admin.site.register(StudentGroup)
admin.site.register(Student)
admin.site.register(Spravka)
admin.site.register(Scholarship)
