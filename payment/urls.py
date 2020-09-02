from django.urls import path
from .views import *

urlpatterns = [
    # PAGOS PARA ESTUDIANTES
    path('student/list/<str:pk>/', list_payments_for_students, name = 'list_payments_for_students'),
    path('student/create/', create_payment, name= 'create_payment')
]
