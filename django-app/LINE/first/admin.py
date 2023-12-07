from django.contrib import admin

from .models import Preference,Preference_food,Trip

# Register your models here.

admin.site.register(Preference)
admin.site.register(Preference_food)
admin.site.register(Trip)

#admin.site.register(login_info)