from django.urls import path
from . import views
import membership   #[2]

"""
[2] onad | 20200324 | Created this file
[3] onad | 20200326 | Improvement of [2]
"""

urlpatterns = [
    path('', views.home, name='report_home')   #[3]
]