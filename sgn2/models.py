import os
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import ForeignKey


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


class Company(models.Model):
    name = models.CharField('Название', max_length=64, null=False)
    logo = models.ImageField('Логотип', upload_to=get_upload_path, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "компании"
        verbose_name = "компания"


class Discipline(models.Model):
    name = models.CharField('Название', max_length=64)
    semester = models.ForeignKey('Plan', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "дисциплины"
        verbose_name = "дисциплина"


class Plan(models.Model):
    number = models.IntegerField('Номер семестра', unique=True)

    def __str__(self):
        return f"Семестр {self.number}"

    class Meta:
        verbose_name_plural = "семестры"
        verbose_name = "семестр"

