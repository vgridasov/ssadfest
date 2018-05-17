from django.db import models
from django.contrib import admin

class Team(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'Название')
    regdate = models.DateField(auto_now_add=True, verbose_name=u'Дата регистрации')
    tent_num = models.PositiveSmallIntegerField(default=1, verbose_name=u'Количество мест')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'regdate')


class Member(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=50, default='Безымянный Гость', verbose_name=u'Фамилия, Имя')
    phone = models.CharField(max_length=20, verbose_name=u'Телефон')
    city = models.CharField(max_length=50, default='Малые #беня', verbose_name=u'Город (нас. пункт)')
    company = models.CharField(max_length=50, default='Частное лицо', verbose_name=u'Организация')
    specialization = models.CharField(max_length=100, default='Ламер', verbose_name=u'Специализация в ИТ')
    regdate = models.DateField(auto_now_add=True, verbose_name=u'Дата регистрации')
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Участник команды')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'regdate')


class TeamLeader(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    leader = models.ForeignKey('Member', on_delete=models.CASCADE)
