# chat/models.py

from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Konuşma {self.id} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"


class Message(models.Model):
    SENDER_CHOICES = (
        ('user', 'Kullanıcı'),
        ('bot', 'Chatbot'),
    )

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_sender_display()}: {self.content[:50]}..."

    class Meta:
        ordering = ['timestamp']


class Feedback(models.Model):
    RATING_CHOICES = (
        (1, '1 - Çok Kötü'),
        (2, '2 - Kötü'),
        (3, '3 - Orta'),
        (4, '4 - İyi'),
        (5, '5 - Çok İyi'),
    )

    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Değerlendirme: {self.rating}/5 - {self.message.content[:30]}..."