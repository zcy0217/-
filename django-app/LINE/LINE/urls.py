"""LINE URL Configuration

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
from first import views  
# from django.conf.urls import url
from first.views import CustomLoginView,log_out_view,index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefer_form/', views.prefer_form, name='prefer_form'),
    # path('regist/', registCreateView.as_view() , name = 'regist'),
    #path('finish/', FinishView.as_view() , name = 'finish'),
    #path('prefer/', preferView.as_view() , name = 'prefer'),
    # path('sign_up/', views.SignUpView.as_view(), name = "sign_up"),
    #path('login/', views.login_View.as_view(), name='login'),
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('log_out/', log_out_view.as_view(), name='log_out'),
    path('prefer2/', views.prefer2_view, name='prefer2'),
    #path('user_preferences/', user_preferences, name='user_preferences'),
    path('sign_up/', views.sign_up ,name='sign_up'),
    path('index/', index_view.as_view(), name='index'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('save_trip/', views.save_trip, name='save_trip'),
    path('trip_list/', views.trip_list, name='trip_list'),
    path('trip/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('trip_delete/<int:trip_id>/', views.trip_delete, name='trip_delete'),
]


