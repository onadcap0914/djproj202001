from django.shortcuts import render
"""
[2] onad | 20200324 | File first update
[3] onad | 20200326 | improvement of [2]
"""
# Create your views here.


def home(request):
    # title = 'CEU CCI - Loan Management System'
    # return render(request, 'home.html', {'title': title})   #[3]
    return render(request, 'base_bootstrap_hdr_stky-ftr.html')
