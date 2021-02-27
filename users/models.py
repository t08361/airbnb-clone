from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#User라는 모델 클래스 생성 이걸 이용해 다양한 객체를 만들거임
class User(AbstractUser):
    #성별에 대한 선택목록
    GENDER_MALE="male"
    GENDER_FEMALE="female"
    
    GENDER_CHOICES=(
        (GENDER_FEMALE, "Female"),
        (GENDER_MALE, "Male"),
    )

    #사용 언어에 대한 선택목록
    LANGUAGE_ENGLISH="Enlish"
    LANGUAGE_KOREAN="Korean"

    LANGUAGE_CHOICES=(
        (LANGUAGE_ENGLISH,"English"),
        (LANGUAGE_KOREAN,"Korean")
    )
    
    #사용 화폐에 대한 선택목록
    CURRENCY_USD="usd"
    CURRENCY_KRW="krw"

    CURRENCY_CHOICES=(
        (CURRENCY_USD,"usd"),
        (CURRENCY_KRW,"krw")
    )

    #손님 이용자에 대한 객체중에 속성에 해당하는 것들 (객체는 속성 또는 메소드를 갖는다.)
    """Custom User Model"""

    avatar=models.ImageField(null=True, blank=True)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=10, null=True, blank=True)
    bio=models.TextField(default='', blank=True)
    birthdate=models.DateField(null=True)
    language=models.CharField(choices=LANGUAGE_CHOICES,max_length=10,null=True,blank=True)
    currency=models.CharField(choices=CURRENCY_CHOICES,max_length=10,null=True,blank=True)
    superhost=models.BooleanField(default=False)