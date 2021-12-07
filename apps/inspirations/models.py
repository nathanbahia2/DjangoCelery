from django.db import models


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'Message #{ self.id }'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
