from django.shortcuts import render

# Create your views here.

from django.views import View


class Main(View):
    def get(self, request):
        return render(request, 'fsgn/main_page.html')


class History(View):
    def get(self, request):
        return render(request, 'fsgn/history.html')


class Applicant(View):
    def get(self, request):
        return render(request, 'fsgn/applicant.html')


class Science(View):
    def get(self, request):
        return render(request, 'fsgn/science_work.html')


class Postgraduate(View):
    def get(self, request):
        return render(request, 'fsgn/postgraduate.html')
