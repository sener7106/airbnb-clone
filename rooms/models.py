from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.
class Room(core_models.TimeStampModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)  # 필수 사항
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default="false")
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # 다른 모델과 연결시켜주는 역할... 관계형 데이터베이스, manyrooms one user


# 국가 사용 코드.. django-counries
