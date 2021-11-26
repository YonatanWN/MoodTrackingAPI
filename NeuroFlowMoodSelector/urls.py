"""NeuroFlowMoodSelector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from moodtracker import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name = "register"),
    path('api-auth/', include('rest_framework.urls')),
    path('', include("django.contrib.auth.urls")),
    path('mood/', v.MoodList.as_view(), name="moodlist"),
    path('mood/<int:pk>', v.MoodInputDetail.as_view(),name="mooddetail"),
    path('', v.redirecttomood, name="moodredirect"),
    path('moodUserFriendly/',v.home, name = "home"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
