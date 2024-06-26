from django.contrib import admin
from .models import Teacher, Advantage


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'role', 'photo']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['description']
