from django.shortcuts import render
"""
[2] onad | 20200324 | File first update
"""
# Create your views here.


def home(request):
    return render(request, 'report_home.html')
