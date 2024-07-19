from django.db import models

class Post(models.Model):
    title=models.CharField('タイトル',max_length=20)
    text=models.TextField('本文',max_length=140)
    thumbnail = models.ImageField('画像（空欄可）', upload_to='thumbnails/', null=True, blank=True)
    created_at=models.DateTimeField('日付',auto_now_add=True)
    update_at=models.DateTimeField('更新日',auto_now=True)
    
    def __str__(self):
        return self.title