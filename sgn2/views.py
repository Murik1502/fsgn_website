# Create your views here.
from django.shortcuts import render
# Create your views here.

from django.views import View

from .vk_parser import get_posts

from .models import Teacher, Advantage


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
        return render(request, 'sgn2/applicant.html', context={'info': data})

class History(View):
    def get(self, request):
        data = get_posts()
        return render(request, 'sgn2/about.html', context={'info': data})