from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from wine.models import Wine
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=50)
    content = models.TextField('내용')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, 
            verbose_name='Owner', null=True)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, 
            verbose_name='와인', null=True)
    rating = models.IntegerField(
                validators=[
                    MaxValueValidator(5),
                    MinValueValidator(1)
                ],
                default=5
            )

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'review_posts' # 테이블명 재정의
        ordering = ('-modify_dt',) # orderby 절, -이면 내림차순

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # 현재 데이터의 절대 경로 추출
        return reverse('review:detail', args=(self.id,))
    
    def get_previous(self): # 이전 데이터 추출
        return self.get_previous_by_modify_dt()
    
    def get_next(self): # 다음 데이터 추출
        return self.get_next_by_modify_dt()
