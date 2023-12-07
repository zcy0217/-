from django.shortcuts import render
from django.views.generic import TemplateView #串接HTML
# Create your views here.

class home(TemplateView): #串接HTML
    template_name = 'home.html'

class login(TemplateView): #串接HTML
    template_name = 'login.html'

class prefer_form(TemplateView):
    template_name = 'prefer_form.html'

class sign_up(TemplateView):
    template_name = 'sign_up.html'

class result(TemplateView):
    template_name = 'result.html'

class detailinfo(TemplateView):
    template_name = 'detailinfo.html'

class detailinfoModal(TemplateView):
    template_name = 'detailinfoModal.html'

class tripmanagement(TemplateView):
    template_name = 'tripmanagement.html'
