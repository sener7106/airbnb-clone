from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):  # name을 위한 item
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):  # House rules, ammenity.. 부가 옵션
    class Meta:
        verbose_name = "Room Type"
        ordering = ["created"]


class Amenity(AbstractItem):

    """Amenity Object Definition"""

    class Meta:
        # can configure many Things
        # 모든 모델 클래스 내에 있는 클래스, not inherited
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Object Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Object Definition"""

    class Meta:
        verbose_name = "House Rule"


# Create your models here.


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)


class Room(core_models.TimeStampedModel):

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
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # 폭포수 효과.. 하나가 지워지면 모든 정보가 사라짐
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    # 다른 모델과 연결시켜주는 역할... 관계형 데이터베이스, manyrooms one user
    amenities = models.ManyToManyField("Amenity", blank=True)
    facility = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    # 국가 사용 코드.. django-counries
    # take a class = > string __str__

    def __str__(self):
        return self.name
