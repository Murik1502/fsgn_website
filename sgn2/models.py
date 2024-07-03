import os
from django.db import models
from django.db import transaction


def get_upload_path(instance, filename):
    if isinstance(instance, Teacher):
        return os.path.join('photos/teachers', "%s" % instance.name, filename)
    elif isinstance(instance, Company):
        return os.path.join('companies', "%s" % instance.name, filename)


class Teacher(models.Model):
    name = models.CharField('ФИО', max_length=32)
    role = models.CharField('Должность', max_length=64)
    description = models.TextField('Описание', max_length=2048)
    photo = models.ImageField('Фото', upload_to=get_upload_path, blank=True)

    def __str__(self):
        return f"{self.name}"

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
    logo = models.FileField('Логотип', upload_to=get_upload_path, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "компании"
        verbose_name = "компания"


class BachelorPlan(models.Model):
    number = models.IntegerField('Номер семестра', unique=True)

    def __str__(self):
        return f"Семестр {self.number}"

    class Meta:
        verbose_name_plural = "Учебный план (бакалавриат)"
        verbose_name = "Учебный план (бакалавриат)"


class MasterPlan(models.Model):
    number = models.IntegerField('Номер семестра', unique=True)

    def __str__(self):
        return f"Семестр {self.number}"

    class Meta:
        verbose_name_plural = "Учебный план (магистратура)"
        verbose_name = "Учебный план (магистратура)"


class BachelorDiscipline(models.Model):
    name = models.CharField('Название', max_length=64)
    bachelor_semester = models.ForeignKey(BachelorPlan, on_delete=models.SET_NULL, null=True, blank=True,
                                          related_name='disciplines')


class MasterDiscipline(models.Model):
    name = models.CharField('Название', max_length=64)
    master_semester = models.ForeignKey(MasterPlan, on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name='disciplines')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "дисциплины"
        verbose_name = "дисциплина"


class BachelorStatistics(models.Model):
    passing_score = models.IntegerField('Проходной балл', null=True)
    average_score = models.IntegerField('Средний проходной балл', null=True)
    budget_places = models.IntegerField('Бюджетные места', null=True)
    subject1_min_score = models.IntegerField('Минимальный балл по математике', null=True)
    subject2_min_score = models.IntegerField('Минимальный балл по информатике/истории/математике', null=True)
    subject3_min_score = models.IntegerField('Минимальный балл по русскому языку', null=True)

    def __str__(self):
        return f"Условия поступления (бакалавриат)"

    class Meta:
        verbose_name_plural = "условия поступления (бакалавриат)"
        verbose_name = "условия поступления (бакалавриат)"


class MasterStatistics(models.Model):
    passing_score = models.IntegerField('Проходной балл', null=True)
    budget_places = models.IntegerField('Бюджетные места', null=True)

    def __str__(self):
        return f"Условия поступления (магистратура)"

    class Meta:
        verbose_name_plural = "условия поступления (магистратура)"
        verbose_name = "условия поступления (магистратура)"
