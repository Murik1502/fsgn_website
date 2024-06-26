# Create your views here.
from django.shortcuts import render
# Create your views here.

from django.views import View

from .vk_parser import get_posts

from .models import Teacher, Advantage, Plan, Discipline


class About(View):
    def get(self, request):
        data = get_posts()
        teachers = Teacher.objects.all()
        advantages = Advantage.objects.all()
        return render(request, 'sgn2/about.html', context={
            'info': data,
            'teachers': teachers,
            'advantages': advantages
        })


class Applicant(View):
    def get(self, request):
        data = get_posts()
        # semesters = Plan.objects.order_by('number')
        # for semester in semesters:
        #     discs = Discipline.objects.filter(semester=semester)
        return render(request, 'sgn2/applicant.html', context={'info': data})


class History(View):
    def get(self, request):
        data = get_posts()
        return render(request, 'sgn2/about.html', context={'info': data})
