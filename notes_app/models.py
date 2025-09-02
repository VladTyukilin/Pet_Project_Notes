from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Добавь эту строку

    class Meta:
        verbose_name = 'ЗАМЕТКИ'
        verbose_name_plural = 'ЗАМЕТКИ'

    def __str__(self):
        return self.title
