from django.db import models


class Topic(models.Model):

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'

    name = models.TextField(max_length=200, verbose_name='Заголовок')
    created_at = models.DateTimeField(
        verbose_name='Создан',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Обновлен',
        auto_now=True
    )

    def __str__(self):
        return self.name


class Entry(models.Model):

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Заголовок')
    text = models.TextField(max_length=1000, verbose_name='Текст')
    created_at = models.DateTimeField(
        verbose_name='Создан',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Обновлен',
        auto_now=True
    )

    def __str__(self):
        return f"{self.text[:50]}..."
