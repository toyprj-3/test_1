from django.db import models
from users.models import User



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)             # 제목 (최대 길이 70자)
    content = models.TextField(blank=True)  # 본문 내용
    datetime = models.DateTimeField(auto_now_add=True)  # 현재 시간 자동저장
    image = models.ImageField(upload_to="post/images/%Y/%m/%d/", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"[self.pk]{self.title}"

    def get_absolute_url(self):
        return f"/posts/{self.pk}/"