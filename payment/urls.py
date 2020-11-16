from django.urls import path
from .views import *

urlpatterns = [
    # PAGOS PARA ESTUDIANTES
    path('student/list/<str:pk>/', list_payments_for_students, name = 'list_payments_for_students'),
    path('student/create/', create_payment, name= 'create_payment'),
    path('student/create/manual/', create_payment_manual, name='create_payment_manual'),
    path('student/delete/manual/<str:pk>/', delete_payment_manual, name = 'delete_payment_manual'),
    # COMPROMISOS DE PAGO
    path('compromise/create/', create_compromise, name= 'create_compromise'),
]
