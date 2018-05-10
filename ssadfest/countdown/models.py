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
    name = models.CharField(max_length=50, default='Безымянный Гость')
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50, default='Малые #беня')
    company = models.CharField(max_length=50, default='Частное лицо')
    specialization = models.CharField(max_length=100, default='Ламер')
    regdate = models.DateField(auto_now_add=True)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'regdate')


class TeamLeader(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    leader = models.ForeignKey('Member', on_delete=models.CASCADE)
