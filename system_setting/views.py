from django.shortcuts import render, redirect
from django.template import context

from system_setting.forms import CampusForm  # forms.py
from system_setting.models import Campus  # models.py
import datetime

"""
[2] onad | 20200324 | File first update
[3] onad | 20200326 | Improvement of [2]
[13] onad | 20200525 | Create Campus MVT with CRUD
"""


# Create your views here.


def home(request):
    title = 'System Setting'
    return render(request, 'system_setting_home.html', {'title': title})  # [3]


# [13] /system_setting/campus
def campus(request):
    title = 'Campus'
    campuses = Campus.objects.all()
    return render(request, 'campus_home.html', {'title': title,
                                                'campuses': campuses})


# [13]
def upsert(request):
    title = 'Add New Campus'
    #
    if request.method == "POST":
        form = CampusForm(request.POST)
        # form.fields['registered_by'] = request.user.username
        # form.fields['registered_date'] = datetime.datetime.now().strftime("%Y%m%d")
        # form.fields['updated_by'] = request.user.username
        # form.fields['updated_date'] = datetime.datetime.now().strftime("%Y%m%d")
        if form.is_valid():
            try:
                form.save()
                return redirect('/system_setting/campus')
            except:
                pass
    else:
        form = CampusForm()
        # context['form_errors'] = form.errors
        return render(request, 'upsert.html', {'form': form, 'title': title})
