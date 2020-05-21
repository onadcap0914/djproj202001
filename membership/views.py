from django.shortcuts import render
"""
[2] onad | 20200324 | File first update
[3] onad | 20200326 | Improvement of [2]
"""
# Create your views here.


def home(request):
    # return HttpResponse("Hellow World")   #[2] removed this and replaced with the next line
    title = 'Membership'
    return render(request, 'membership_home.html', {'title': title})    #[3]

