from django.db import models
from django.db.models.functions import Now
# Create your models here.


class Post(models.Model):
    #PK : 'id' 라는 이름으로 자동 생성된다.
    subject = models.CharField(max_length = 200) # 글제목
    user = models.CharField(max_length = 20) # 작성자, 필수(NN)
    content = models.TextField() # 글내용, null 허용
    view_cnt = models.IntegerField(default = 0) # 조회수, 기본값 0
    reg_date = models.DateTimeField(default = Now()) # 작성일시, 기본값 현재시간


    def __str__(self) :
        return f'{self.id} : {self.subject}'
    

