from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(black=True)
    cover = models.ImageField(upload_to="covers") #Тут повине бути фото обкладенки
    file = models.FileField(upload_to="files")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    