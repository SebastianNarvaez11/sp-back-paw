from django.urls import path
from .views import *

urlpatterns = [
    path('email/', send_email, name= 'send_email'),
    path('sms/', send_sms, name='send_sms'),
    path('wpp/', send_wpp, name='send_wpp'),
    path('sms/massive/', send_sms_massive, name='send_sms_massive'),
    path('email/massive/', send_email_massive, name='send_email_massive')
]
