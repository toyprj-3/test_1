from django.db import models

# 사용자 정보 추가
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserMangager


# 장고 모델이 db로 처리 날릴 때 관리 (일반 유저, 슈퍼유저, 스테프 )
class UserManager(DjangoUserMangager):
    def _create_user(self, username, email, password, **extra_fields):
        
        # 이메일 값이 꼭 필요한 경우
        # if not email:
        #     raise ValueError('이메일이 없습니다. 이메일을 꼭 입력해주세요')
        
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(verbose_name='전화번호', max_length=11)
    
    objects = UserManager()
    
    
# 사용자 확장 정보
# class UserInfo(models.Model):
#     phone_sub = models.CharField(verbose_name='보조 전화번호', max_length=11)
    
#     user = models.ForeignKey(to='User', on_delete=models.CASCADE)