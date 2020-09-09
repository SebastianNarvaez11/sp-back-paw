from django.urls import path
from .views import *

urlpatterns = [
    path('email/', send_email, name= 'send_email'),
]
