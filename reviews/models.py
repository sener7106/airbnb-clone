from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):
    """Review Model Definitions"""

    review = models.TextField()
    accuracy = models.IntegerField(default=5)
    communication = models.IntegerField(default=5)
    cleanliness = models.IntegerField(default=5)
    location = models.IntegerField(default=5)
    check_in = models.IntegerField(default=5)
    value = models.IntegerField(default=5)
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room.name}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg."

    # python 3 string 문법
    # set은 foreign key의 대상이 element로 얻는 방법이다.
