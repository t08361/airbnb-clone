from django.db import models

# Create your models here.
#auto뭐시기 저 놈들은 바뀔 때마다 자동으로 수정해주는 친구들
class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
# core라는 모델을 db에 등록하지는 말거라~~따쓱아
    class Meta:
        abstract = True