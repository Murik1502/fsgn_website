from django.shortcuts import render
from django.views import View
from .vk_parser import get_posts
from .models import Teacher, Advantage, BachelorPlan, MasterPlan, Company, BachelorStatistics, MasterStatistics

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
        bachelor_semesters = BachelorPlan.objects.prefetch_related('disciplines').all()
        master_semesters = MasterPlan.objects.prefetch_related('disciplines').all()
        bachelor_statistics = BachelorStatistics.objects.all()
        master_statistics = MasterStatistics.objects.all()
        return render(request, 'sgn2/applicant.html', context={
            'info': data,
            'companies': companies,
            'bachelor_semesters': bachelor_semesters,
            'master_semesters': master_semesters,
            'bachelor_statistics': bachelor_statistics,
            'master_statistics': master_statistics,
        })

class History(View):
    def get(self, request):
        data = get_posts()
        return render(request, 'sgn2/about.html', context={'info': data})
