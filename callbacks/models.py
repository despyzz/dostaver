from django.db import models


# Create your models here.

class CallbackRequests(models.Model):
    telephone = models.TextField()
    callback_type = models.TextField()

    class Meta:
        verbose_name_plural = 'CallbackRequests'

    def __str__(self):
        return f'[{self.id}] {self.telephone}'
