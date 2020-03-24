"""djproj202001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
[1] onad | 20200323 | Activate Python Django Admin Interface
[2] onad | 20200324 | Adding the modules' urls
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),    #[1]
    path('', views.home),
    path('membership/', include('membership.urls')),    #[2] start
    path('accounting/', include('accounting.urls')),
    path('transaction/', include('transaction.urls')),
    path('system_setting/', include('system_setting.urls')),
    path('report/', include('report.urls')),    #[2] end
]
