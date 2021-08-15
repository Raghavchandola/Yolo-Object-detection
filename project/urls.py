from os import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('signuppage', views.signuppage, name='signuppage'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('classes', views.classes, name='classes'),
    path('faq', views.faq, name='faq'),
    path('paying', views.paying, name='paying'),
    path('success', views.success, name='success'),
    path('opened_notes/<sub>/', views.opened_notes, name='opened_notes'),
    path('opened_dash/<pk_test>/', views.opened_dash, name='opened_dash'),
    path('opened_subject/<test>/', views.opened_subject, name='opened_subject'),
    path('opened_chapter/<sub_test>/',
         views.opened_chapter, name='opened_chapter'),
    #path('opened_notes/<sub>/', views.opened_notes, name='opened_notes'),
    path('test', views.test, name='test'),
    path('test1', views.test1, name='test1'),
    path('certificate', views.certificate, name='certificate'),
    path('level', views.level, name='level'),
    path('accent', views.accent, name='accent'),
    path('initial', views.initial, name='initial'),
    path('opening', views.opening, name='opening'),
    path('displaying/<int:pk>', views.displaying, name='displaying')

]
