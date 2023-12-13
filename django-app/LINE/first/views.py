#from django.shortcuts import render
from datetime import datetime
from .models import Preference
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.contrib import auth
from django.contrib.auth import authenticate,login, logout
from .forms import PreferenceForm,Preference_food_Form,CustomUserCreationForm 
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from vendor.filters import Travel_Filter
from vendor import models

#FBVs的方法
def home(request):
    # 在此编写用于呈现首页内容的逻辑

    #Search Function
    data = models.Main.objects.all().order_by('-star')
    Filters = Travel_Filter(queryset = data)

    if request.method == 'POST': #user input
        Filters = Travel_Filter(request.POST, queryset = data)

    return render(request, 'home.html', {
        'Filters' : Filters,
    })

   




from django.shortcuts import render, redirect
from .models import Preference, Preference_food
from .forms import PreferenceForm, Preference_food_Form

from django.contrib.sessions.models import Session

@login_required
def prefer_form(request):
    user = request.user
    try:
        preferences = Preference.objects.get(fk1=user)
    except Preference.DoesNotExist:
        preferences = None

    try:
        preferences_food = Preference_food.objects.get(fk2=user)
    except Preference_food.DoesNotExist:
        preferences_food = None

    if request.method == 'POST':
        form = PreferenceForm(request.user, request.POST, instance=preferences)
        form_food = Preference_food_Form(request.user, request.POST, instance=preferences_food)

        if form.is_valid() and form_food.is_valid():
            preferences = form.save(commit=False)
            preferences.fk1 = request.user  # 关联当前用户
            preferences.save()

            preferences_food = form_food.save(commit=False)
            preferences_food.fk2 = request.user  # 关联当前用户
            preferences_food.save()

            # 将用户的偏好设置保存在会话中
            request.session['user_preferences'] = preferences
            request.session['user_preferences_food'] = preferences_food

            return render(request, 'prefer2.html', {'preferences': preferences, 'preferences_food': preferences_food})

    else:
        # 尝试从会话中获取之前保存的偏好设置数据
        preferences = request.session.get('user_preferences', preferences)
        preferences_food = request.session.get('user_preferences_food', preferences_food)

        form = PreferenceForm(request.user, instance=preferences)
        form_food = Preference_food_Form(request.user, instance=preferences_food)

    return render(request, 'prefer_form.html', {'form': form, 'form_food': form_food})














class CustomLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.authentication_form(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # 成功登录后重定向到首页
            return redirect('index')
        else:
            # 验证失败，显示错误消息
            error_message = "名稱或密碼有誤!"
            return render(request, self.template_name, {'error_message': error_message})
    



class log_out_view(TemplateView):
    template_name = 'log_out.html'  # 指定要呈现的模板

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super().get(request, *args, **kwargs)

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('registration_success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})



def registration_success(request):
    return redirect('prefer_form') 

@login_required
def prefer2_view(request):
    user = request.user
    try:
        preferences = Preference.objects.get(fk1=user)
    except Preference.DoesNotExist:
        preferences = None

    try:
        preferences_food = Preference_food.objects.get(fk2=user)
    except Preference_food.DoesNotExist:
        preferences_food = None
    print(preferences, preferences_food)
    return render(request, 'prefer2.html', {'preferences': preferences, 'preferences_food': preferences_food})
    


class index_view(TemplateView):
    template_name = 'index.html'  # 指定要呈现的模板    


from django.shortcuts import render, redirect
from .models import Trip
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404

@login_required
def save_trip(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        locations = request.POST.get('locations')
        sorted_locations = request.POST.get('sorted_locations')

        # 檢查使用者是否已經擁有同名的行程，如果有就更新，沒有就創建新的行程
        trip, created = Trip.objects.get_or_create(user=request.user, title=title, defaults={'locations': locations})

        # 如果行程已經存在，則更新地點和日期時間
        if not created:
            trip.locations = locations

        # 設定已排序的位置列表
        trip.sorted_locations = sorted_locations

        trip.datetime = timezone.now()
        trip.save()

        return redirect('trip_list')

    return render(request, 'index.html')




@login_required
def trip_list(request):
    trips = Trip.objects.filter(user=request.user).order_by('-datetime')
    context = {'trips': trips}
    return render(request, 'trip_list.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Trip



def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    locations_list = trip.locations.split(',')  # 將 locations 字串轉換為列表
    return render(request, 'trip_detail.html', {'trip': trip, 'locations_list': locations_list})


from django.http import JsonResponse

@login_required
def trip_delete(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)

    if request.method == 'POST':
        trip.delete()
        return JsonResponse({'message': '行程已刪除'}, status=200)

    return JsonResponse({'message': '無效的請求'}, status=400)

# @login_required
# def trip_list(request):
#     trips = Trip.objects.filter(user=request.user)
#     for trip in trips:
#         trip.locations_list = trip.locations.split(',')
#     context = {'trips': trips}
#     return render(request, 'trip_list.html', context)