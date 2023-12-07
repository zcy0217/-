from django import forms
from .models import Preference,Preference_food
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("您輸入的確認密碼與密碼不符")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("此名稱已存在")
        return username
    
    
class PreferenceForm(forms.ModelForm):
    
    class Meta:
        model = Preference
        fields = ['choice1', 'choice2', 'choice3','choice4']
    def __init__(self, user, *args, **kwargs):
        super(PreferenceForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super(PreferenceForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance        
    

class Preference_food_Form(forms.ModelForm):
    
    class Meta:
        model = Preference_food
        fields = ['choice5', 'choice6']
    def __init__(self, user, *args, **kwargs):
        super(Preference_food_Form, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super(Preference_food_Form, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance      