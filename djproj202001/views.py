from django.shortcuts import render
"""
[2] onad | 20200324 | File first update
[3] onad | 20200326 | improvement of [2]
[4] onad | 20200330 | Application Home page and sign up functionality
"""
# Create your views here.


def home(request):
    title = 'CEU Credit Cooperative Management System'
    return render(request, 'home.html', {'title': title})   #[3] [4]

