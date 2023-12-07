"""
URL configuration for LINE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from first.views import home,login,prefer_form,sign_up,result,detailinfo,detailinfoModal,tripmanagement #串接HTML
# from django.conf.urls import url

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('',home.as_view(),name='')
    path('',home.as_view(),name='home'), #串接HTML
    path('login/',login.as_view(),name='login'),
    path('prefer_form/',prefer_form.as_view(),name='prefer_form'),
    path('sign_up/',sign_up.as_view(),name='sign_up'),
    path('result/',result.as_view(),name='result'),
    path('detailinfo/',detailinfo.as_view(),name='detailinfo'),
    path('detailinfoModal',detailinfoModal.as_view(),name='detailinfoModal'),
    path('tripmanagement/',tripmanagement.as_view(),name='tripmanagement'),
]