# views.py

from django.shortcuts import render
from django.views import View
from .vk_parser import get_posts
from .models import Teacher, Advantage, BachelorPlan, MasterPlan, BachelorCompany, MasterCompany, BachelorStatistics, \
    MasterStatistics


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
        bachelor_companies = BachelorCompany.objects.all()
        master_companies = MasterCompany.objects.all()
        bachelor_semesters = BachelorPlan.objects.prefetch_related('disciplines').all()
        master_semesters = MasterPlan.objects.prefetch_related('disciplines').all()
        bachelor_statistics = BachelorStatistics.objects.all()
        master_statistics = MasterStatistics.objects.all()

        total_columns = 2
        bachelor_num_semesters = len(bachelor_semesters)
        bachelor_rows = (len(bachelor_semesters) + 1) // total_columns
        reordered_bachelor_semesters = [None] * bachelor_num_semesters

        if bachelor_num_semesters != 0:
            for index in range(bachelor_num_semesters):
                row = index % bachelor_rows
                column = index // bachelor_rows
                new_index = row * total_columns + column
                reordered_bachelor_semesters[new_index] = bachelor_semesters[index]

        master_num_semesters = len(master_semesters)
        master_rows = (master_num_semesters + 1) // total_columns
        reordered_master_semesters = [None] * master_num_semesters

        if master_num_semesters != 0:
            for index in range(master_num_semesters):
                row = index % master_rows
                column = index // master_rows
                new_index = row * total_columns + column
                reordered_master_semesters[new_index] = master_semesters[index]

        return render(request, 'sgn2/applicant.html', context={
            'info': data,
            'bachelor_companies': bachelor_companies,
            'master_companies': master_companies,
            'bachelor_semesters': reordered_bachelor_semesters,
            'master_semesters': reordered_master_semesters,
            'bachelor_statistics': bachelor_statistics,
            'master_statistics': master_statistics,
        })


class History(View):
    def get(self, request):
        data = get_posts()
        return render(request, 'sgn2/history.html', context={'info': data})
