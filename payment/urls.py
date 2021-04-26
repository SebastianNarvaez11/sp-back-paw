from django.urls import path
from .views import *

urlpatterns = [
    # PAGOS PARA ESTUDIANTES
    path('student/list/', list_payments, name='list_payments'),
    path('student/list/<str:pk>/', list_payments_for_students,
         name='list_payments_for_students'),
    path('student/create/', create_payment, name='create_payment'),
    path('student/create/manual/', create_payment_manual,
         name='create_payment_manual'),
    path('student/delete/manual/<str:pk>/',
         delete_payment_manual, name='delete_payment_manual'),
    path('period/<str:period>/', payment_filter_period, name='payment_filter_period')
    # COMPROMISOS DE PAGO
    path('compromise/create/', create_compromise, name='create_compromise'),
    path('compromise/update/<str:pk>/', update_compromises,
         name='update_compromises'),  # para los compromisos desde la lista
    path('compromise/update2/<str:pk>/', update_compromises_detail,
         name='update_compromises_detail'),  # para los compromisos desde eldetalle e estudiante
    path('compromise/list/', list_compromises, name='list_compromises'),
    path('compromises/delete/<str:pk>/',
         delete_compromises, name='delete_compromises')
]
