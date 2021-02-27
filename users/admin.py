from django.contrib import admin
from . import models



# Register your models here.

# 관리자 페이지에서 모델User를 관리 할수있는 클래스 설정
# 9번 줄은 10번 클래스가 동작할수있게하는 부분
# list_display는 행으로 보이고자하는거, 
# list_filter는 조건에 따라 선택적인 내용만 얻을 수있게 도와주는애
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    
    """Custom User Admin"""

    list_display=('id','username','gender','language','birthdate','bio','avatar','currency','superhost')
    list_filter=('gender','bio','superhost')

