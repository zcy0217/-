#reference: https://www.learncodewithmike.com/2020/05/django-filter.html

from django import forms
from Project_App.models import Travel_DB
import django_filters as filters

class Travel_Filter(filters.FilterSet):

    address = filters.CharFilter(
        lookup_expr='icontains',
        widget = forms.TextInput(attrs={'class': 'form-control'})
        )

    tag = filters.CharFilter(
        widget=forms.Select(
            choices=(('', '請選擇'),) + Travel_DB.Type_Choices, attrs={'class': 'form-control'})
            )
    
    # cRest_Day = filters.DateFilter

    class Meta:
        model = Travel_DB
        fields = '__all__'