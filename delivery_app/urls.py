# delivery/urls.py
from django.urls import path
from .views import schedule_delivery
from .views import create_delivery
from .views import success_page
urlpatterns = [
    path('schedule/', schedule_delivery, name='schedule_delivery'),
    path('delivery/create/', create_delivery, name='create_delivery'),
    path('success/', success_page, name='success_page')
]
