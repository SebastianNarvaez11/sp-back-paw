from django.urls import path
from .views import *

urlpatterns = [
    path('email/', send_email, name= 'send_email'),
    path('sms/', send_sms, name='send_sms')
]
