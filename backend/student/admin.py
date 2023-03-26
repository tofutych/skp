from django.contrib import admin

from .models import Group, Student


@admin.register(Group)
class GrouptAdmin(admin.ModelAdmin):
    list_display = ("id", "number")
    prepopulated_fields = {"slug": ("number", )}


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname")