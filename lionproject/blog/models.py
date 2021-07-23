from django.db import models

# Create your models here.
class Blog(models.Model):   # Blog라는 이름의 클래스
    title = models.CharField(max_length=200)    # CharField 는 글자수 제한
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()   # DateTimeField는 날짜, 시간
    body = models.TextField()   # TextField는 글자수 제한없음

    def __str__(self):  # title이 뜨게 해줌
        return self.title

    def summary(self):  # summary는 요약을 해주는 메소드
        return self.body[:10]  # body를 10자까지 잘라서 보여줌
