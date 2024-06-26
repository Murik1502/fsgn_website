import os
from django.db import models
from django.contrib.auth.models import User, Group


def get_upload_path(instance, filename):
    return os.path.join('photos/teachers', "%s" % instance.name, filename)


class Teacher(models.Model):
    name = models.CharField('ФИО', max_length=32)
    role = models.CharField('Должность', max_length=64)
    description = models.TextField('Описание', max_length=2048)
    photo = models.ImageField('Фото', upload_to=get_upload_path, blank=True)

    def __str__(self):
        return f"{self.name})"

    class Meta:
        verbose_name_plural = "преподаватели"
        verbose_name = "преподаватель"


class Advantage(models.Model):
    description = models.TextField('Описание', max_length=128)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name_plural = "преимущества"
        verbose_name = "преимущество"
