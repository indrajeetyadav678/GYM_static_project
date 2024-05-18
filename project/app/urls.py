from django.urls import path
from .views import*

urlpatterns=[
    path('',index, name='index'),
    path('about/',about, name='about'),
    path('classlt/',classlt, name='classlt'),
    path('service/',service, name='service'),
    path('team/',team, name='team'),
    path('timetable/',timetable, name='timetable'),
    path('calculate/',calculate, name='calculate'),
    path('gallery/',gallery, name='gallery'),
    path('blog/',blog, name='blog'),
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('contact/',contact, name='contact'),

    # ========= registrationform urls =======
    
    path('registerdata/',registerdata, name='registerdata'),
    path('logindata/',logindata, name='logindata'),
    path('logout/',logout, name='logout'),
    path('editpro/',editpro, name='editpro'),

]