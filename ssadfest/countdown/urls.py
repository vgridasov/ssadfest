from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/new/', views.member_new, name='member_new'),
    path('members/', views.Members.as_view(), name='members'),

]
