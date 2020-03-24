from django.shortcuts import render
"""
[2] onad | 20200324 | File first update
"""
# Create your views here.


def home(request):
    # return HttpResponse("Hellow World")   #[2] removed this and replaced with the next line
    return render(request, 'membership_home.html')
