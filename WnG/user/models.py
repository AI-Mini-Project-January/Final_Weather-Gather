
from pickle import NONE
from tkinter import Image
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin
from django.db import models


# Create your models here.
# 커스텀 유저만들꺼임 -> AbstractBaseUser 이거를 상속받아서 만들면 그게 유저필드가 됨
# 장고에서 기본으로 제공하는 auth_user 안쓰고 커스텀한거 쓰려면 settings 가서 AUTH_USER_MODEL = '내가만든이름.User' 적어줘야함
# TextField는 길이 제한없음, CharField는 길이제한을 써줘야함
# 닉네임 -> 화면에 표기되는 이름
# 아이디 -> 회원가입할 때 사용하는 아이디
# 비밀번호 -> 장고에서 만들어주는걸로 디폴트
# 나이 -> 
# 프로필 사진 저장

class UserManager(BaseUserManager):
    def create_user(self, nickname, profile_image, age, password, **kwargs):
        user = self.model(
            nickname=nickname,
            profile_image=profile_image,
            age=age,
            password=password,
            **kwargs
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, password, profile_imag=NONE, age=NONE, **kwargs):
        user = self.model(
            nickname=nickname,
            age=age,
            is_staff=True, 
            is_superuser=True,
            **kwargs
            )
        user.save(using=self._db)
        return user    


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    nickname = models.CharField(max_length=24,verbose_name='닉네임',null=False,unique=True)
    identi= models.CharField(max_length=24,verbose_name='아이디', unique=True)
    age = models.IntegerField(verbose_name='나이', null=True )
    # profile_image = models.TextField()
    profile_image = models.ImageField(upload_to="board/images", blank=True)
    USERNAME_FIELD = 'nickname'
    # REQUIRED_FIELDS = ['age']
        

    def __str__(self):
        return self.user_id


    profile_image = models.TextField()
    nickname = models.CharField(max_length=24, unique=True)
    identi= models.CharField(max_length=24, unique=True)
    age = models.IntegerField()

# 실제로 유저를 선택하면 그 유저의 이름을 어떤필드를 쓸거냐
    USERNAME_FIELD = 'nickname'
    
# Meta 안해주면 user_user 테이블이 됨
    class Meta:
        db_table = "User"

