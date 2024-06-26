from django.contrib import admin
from .models import Teacher, Advantage, Company, Discipline, Plan


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'role', 'photo']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['description']


class DisciplineInline(admin.TabularInline):
    model = Discipline
    extra = 0


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    inlines = [DisciplineInline]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']
    search_fields = ['name']
