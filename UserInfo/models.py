from django.db import models

class UserInfo(models.Model):
    name = models.CharField('ФИО', max_length=50)
    city = models.CharField('Город проживания', max_length=30)
    job = models.CharField('Место работы', max_length=30)
    date_of_birth = models.DateField('Дата рождения', default='1990-01-01')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

