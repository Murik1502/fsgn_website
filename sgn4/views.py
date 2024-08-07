from django.shortcuts import render
from django.views import View


class Applicant(View):
    def get(self, request):
        return render(request, 'sgn4/applicant.html')
