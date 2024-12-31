
from django.contrib import admin
from .models import phonebook

@admin.register(phonebook)
class PhonebookAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')  # Display name and phone in the admin list view
    search_fields = ('name', 'phone')  # Add search functionality
