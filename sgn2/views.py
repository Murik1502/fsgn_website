from django.shortcuts import render
from django.views import View
from .vk_parser import get_posts
from .models import Teacher, Advantage, BachelorPlan, MasterPlan, Company, BachelorStatistics, MasterStatistics, BachelorProgram, MasterProgram

class About(View):
    def get(self, request):
        data = get_posts()
        teachers = Teacher.objects.all()
        advantages = Advantage.objects.all()
        return render(request, 'sgn2/about.html', context={
            'info': data,
            'teachers': teachers,
            'advantages': advantages,
        })

class Applicant(View):
    def get(self, request):
        data = get_posts()
        companies = Company.objects.all()
        bachelor_programs = BachelorProgram.objects.all().prefetch_related('semesters__disciplines', 'statistics')
        master_programs = MasterProgram.objects.all().prefetch_related('semesters__disciplines', 'statistics')
        return render(request, 'sgn2/applicant.html', context={
            'info': data,
            'companies': companies,
            'bachelor_programs': bachelor_programs,
            'master_programs': master_programs,
        })



class History(View):
    def get(self, request):
        data = get_posts()
        return render(request, 'sgn2/about.html', context={'info': data})
