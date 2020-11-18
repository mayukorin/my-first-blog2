# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:49:02 2020

@author: Mayuko
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
]

