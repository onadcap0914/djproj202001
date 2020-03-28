from django.urls import path
from . import views

"""
[2] onad | 20200324 | Created this file
[3] onad | 20200326 | Improvement of [2]
"""

urlpatterns = [
    path('', views.home, name='system_setting_home'),   #[3]
]