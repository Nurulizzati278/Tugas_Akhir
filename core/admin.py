from django.contrib import admin
from django import forms
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['nip', 'profil', 'nama', 'umur', 'golongan', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('nip', 'nama', 'profil', 'umur', 'golongan')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Password', {'fields': ('password',)}),  # Menambahkan bagian untuk mengelola password
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nip', 'nama', 'profil', 'umur', 'golongan', 'is_active', 'is_staff', 'is_superuser', 'password1', 'password2'),
        }),
    )
    search_fields = ['nip', 'nama']
    ordering = ['nama']

admin.site.register(CustomUser, CustomUserAdmin)
