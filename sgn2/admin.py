from django.contrib import admin
from .models import Teacher, Advantage, Company, Discipline, BachelorPlan, MasterPlan, BachelorStatistics, MasterStatistics

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'role', 'photo']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['description']

class BachelorDisciplineInline(admin.TabularInline):
    model = Discipline
    extra = 0
    can_delete = False

class MasterDisciplineInline(admin.TabularInline):
    model = Discipline
    extra = 0
    can_delete = False

@admin.register(BachelorPlan)
class BachelorPlanAdmin(admin.ModelAdmin):
    inlines = [BachelorDisciplineInline]

@admin.register(MasterPlan)
class MasterPlanAdmin(admin.ModelAdmin):
    inlines = [MasterDisciplineInline]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']
    search_fields = ['name']

@admin.register(BachelorStatistics)
class BachelorStatisticsAdmin(admin.ModelAdmin):
    list_display = ['passing_score', 'average_score', 'budget_places', 'subject1_min_score',
                    'subject2_min_score', 'subject3_min_score']

@admin.register(MasterStatistics)
class MasterStatisticsAdmin(admin.ModelAdmin):
    list_display = ['passing_score', 'budget_places']
