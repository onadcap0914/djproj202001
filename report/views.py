from django.shortcuts import render
"""
[2] onad | 20200324 | File first update
[3] onad | 20200326 | Improvement of [2]
"""
# Create your views here.


def home(request):
    title = 'Report'
    return render(request, 'report_home.html', {'title': title})    #[3]
