from django.contrib import admin

from .models import Student, Teacher, Student_Teachers_Relations

class RelationsInline(admin.TabularInline):
    model = Student_Teachers_Relations
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [RelationsInline]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [RelationsInline]
