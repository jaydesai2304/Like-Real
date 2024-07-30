from django.contrib import admin
from .models import Person, Product, Address, Card, Contact,Cart


class PersonAdmin(admin.ModelAdmin):
    list_display = ("username", "fullname", "email", "phone", "gender")

admin.site.register(Person, PersonAdmin)