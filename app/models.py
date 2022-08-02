from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser 사용
class Users(AbstractUser):
    user_auth = models.CharField(max_length=50)
    hint = models.CharField(max_length=50)


# 작성, 수정 시간을 상속
class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Books(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(Users, on_delete=models.CASCADE)
    img = models.FileField(upload_to="", blank=True)
    keyword = models.CharField(max_length=100)
    publication = models.DateTimeField()
    page = models.IntegerField()
    price = models.IntegerField()
