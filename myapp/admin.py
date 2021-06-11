from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "salary", "phone")
