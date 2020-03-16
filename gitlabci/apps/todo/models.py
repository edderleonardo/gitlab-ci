from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ToDo(models.Model):
    name = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.name
