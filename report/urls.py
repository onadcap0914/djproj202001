from django.urls import path
from . import views
import membership   #[2]

"""
[2] onad | 20200324 | Created this file
"""

urlpatterns = [
    path('', views.home, name='home')
]