from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)             # 제목 (최대 길이 70자)
    content = models.TextField                          # 본문 내용
    datetime = models.DateTimeField(auto_now_add=True)  # 현재 시간 자동저장