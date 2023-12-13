#reference: https://www.learncodewithmike.com/2020/05/django-filter.html

from django import forms
from vendor.models import Main
import django_filters as filters

class Travel_Filter(filters.FilterSet):

    #目的地城市（沒辦法搜尋地點名稱name欄位，只有address）
    address = filters.CharFilter(
        lookup_expr='icontains',
        widget = forms.TextInput(attrs={'class': 'form-control'})
        )
    
    #日期
    date_input = filters.CharFilter(
        field_name='restday',
        lookup_expr='icontains',
        exclude = True,
        method='turn_day_to_week',
        widget = forms.widgets.DateInput(attrs = {'class': 'form-control', 'type': 'date'})
        )

    
    #（日期）轉換成中文星期函式
    def turn_day_to_week(self, querset, name, value):
        from datetime import datetime

        weekdays_chinese = ['週一', '週二', '週三', '週四', '週五', '週六', '週日']


        date_object = datetime.strptime(value, '%Y-%m-%d')
        day_to_week_index = date_object.weekday() # 取得星期幾的索引，0代表星期一，1代表星期二，以此類推
        day_to_week = weekdays_chinese[day_to_week_index]
        return querset.exclude(restday__icontains = day_to_week)


    #旅遊型態
    travel_type = filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.Select(
            choices=(('', '請選擇'),) + Main.Type_Choices, attrs={'class': 'form-control', 'id': 'travelTypeSelect', 'aria-label': 'Floating label select example'})
            )

    #美食種類
    food_type = filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.Select(
            choices=(('', '請選擇'),) + Main.Food_Choices, attrs={'class': 'form-control', 'id': 'foodTypeSelect'})
            )
    





    #排序方式
    # order = (
    #     ('免費優先', '免費優先'),
    #     ('需要門票優先', '需要門票優先'),
    # )

    # ordering = filters.CharFilter(
    #     label = 'ordering',
    #     method = 'filter_by_ordering',
    #     widget = forms.Select(
    #         choices = (('', '請選擇'),) + order, attrs = {'class': 'form-select', 'id': 'sortingSelect'}
    #     )
    #     )
    # #排序函式
    # def filter_by_ordering(self, querset, name, value):
    #     expression = 'price' if value == '免費優先' else '-price'
    #     return querset.order_by(expression)

    # cRest_Day = filters.DateFilter

    class Meta:
        model = Main
        fields = '__all__'