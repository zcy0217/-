from django.db import models

# Create your models here.
class Vendor(models.Model):
	vendor_name = models.CharField(max_length = 20) # 攤販的名稱
	store_name = models.CharField(max_length = 10) # 攤販店家的名稱
	phone_number = models.CharField(max_length = 20) # 攤販的電話號碼
	address = models.CharField(max_length = 100) # 攤販的地址

class Food(models.Model):
	food_name = models.CharField(max_length = 30) # 食物名稱
	price_name = models.DecimalField(max_digits = 3, decimal_places=0) # 食物價錢
	food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # 代表這食物是由哪一個攤販所做的

class Main(models.Model):

    #旅遊類型選擇
    Type_Choices = (
        ('1', '親子場所'),
        ('2', '團體出遊'),
        ('3', '室內活動'),
        ('4', '室外活動'),
    )
	
    #食物類型選擇
    Food_Choices = (
		('1', '餐廳美食'),
		('2', '街邊小吃'),
    )

    name = models.CharField(max_length = 50, null = False) #名稱
    staytime = models.CharField(max_length = 20, null = True) #停留時間
    blogsrc = models.CharField(max_length = 1024, null = True) #部落格網址
    summary = models.CharField(max_length = 1024, null = True) #簡介
    city = models.CharField(max_length = 5, null = False) #城市
    address = models.CharField(max_length = 256, null = False, default = '') #地址
    tel = models.CharField(max_length = 20, null = True) #電話
    time = models.CharField(max_length = 256, null = True) #營業時間
    remark = models.CharField(max_length = 256, null = True)
    restday = models.CharField(max_length = 20, null = True) #公休日
    website = models.CharField(max_length = 1024, null = True) #網址
    socialwebsite = models.CharField(max_length = 1024, null = True) #社群媒體網址
    star = models.CharField(max_length = 3, null = True, default = '', ) #評分
    price = models.CharField(max_length = 10, default = 0) #價格
    nobarrier = models.CharField(max_length = 1, null = False) #無障礙設施
    parking = models.CharField(max_length = 1, null = False) #停車場
    restaurantfood = models.CharField(max_length = 4, null = True) #餐廳美食
    streetfood = models.CharField(max_length = 4, null = True) #街邊小吃
    child = models.CharField(max_length = 4, null = True) #親子共遊
    group = models.CharField(max_length = 4, null = True) #團體出遊
    indoor = models.CharField(max_length = 4, null = True) #室內活動
    outdoor = models.CharField(max_length = 4, null = True) #室外活動

    travel_type = models.CharField(max_length = 50, null = True) #旅遊類別
    food_type = models.CharField(max_length = 10, null = True) #食物類別