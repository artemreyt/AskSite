from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils import timezone
import os


class Author(models.Model):
    name = models.CharField('Имя автора', max_length=255)
    rating = models.IntegerField('Рейтинг автора', default=0)
    birthday = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class QuestionManager(models.Manager):
    def published(self):
        return self.filter(
            is_published=True,
            datetime_published__lt=timezone.now()
        )


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField('Текст вопроса')
    datetime_published = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField('Опубликована', default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=Author.objects.get(id=1))
    photo = models.ImageField(blank=True, upload_to='question_photo', default='baran.jpg')
    #tags = models.ManyToManyField(to='Tag', blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    objects = QuestionManager()


class Answer(models.Model):
    answer_author = models.CharField('Автор ответа', max_length=50)
    answer_text = models.TextField('Текст ответа')
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)



class Tag(models.Model):
    tag_name = models.CharField('Имя тега', max_length=20)

    class Meta:
        ordering = ('tag_name',)

    def __str__(self):
        return self.tag_name

