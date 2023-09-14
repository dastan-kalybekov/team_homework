from django.contrib.auth import get_user_model
from django.db import models

import telebot
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

bot = telebot.TeleBot('6107937292:AAF6sGWwygfT-YunuLvalkRhtJ-w9_RVmb4', parse_mode=None)

RATINGS = (
    (1, 'Очень плохо'),
    (2, 'Плохо'),
    (3, 'Так себе'),
    (4, 'Хорошо'),
    (5, 'Отлично'),

)


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.post.title} - {self.text[:10]} ..."


class Rating(models.Model):
    rating = models.IntegerField(choices=RATINGS)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return f"{self.post.title} {self.rating}"


@receiver(post_save, sender=Post)
def send_notification(sender, instance, **kwargs):
    if kwargs.get('created'):
        message = f"Твит с названием {instance.title} и текстом {instance.body} успешно создан, пользователь {instance.user.username}"
        bot.send_message(chat_id=instance.user.telegram_chat_id, text=message, parse_mode='html')

    if __name__ == '__main__':
        bot.infinity_polling()
