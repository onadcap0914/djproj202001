from django.urls import path
from . import views

"""
[2] onad | 20200324 | Created this file
[3] onad | 20200326 | Improvement of [2]
[13] onad | 20200525 | Create Campus MVT with CRUD
"""

urlpatterns = [
    path('', views.home, name='system_setting_home'),  # [3]
    path('campus', views.campus, name='campus_home'),  # [13]
    path('upsert', views.upsert, name='campus_upsert'),  # [13]
]
