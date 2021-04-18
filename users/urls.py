from django.urls import path
from .views import *


urlpatterns = [
    # USUARIOS GENERALES
    path('current/', get_current_user, name='get_current_user'),
    path('list/', list_users, name='list_users'),#listado de usuarios generales y admins de una vez
    path('update/<str:pk>/', update_users, name='update_users'),
    path('delete/<str:pk>/', delete_users, name='delete_users'),
    # USUARIOS ADMINISTRADORES
    path('admin/create/', create_users_admin, name='create_user_admin'),
    path('admin/update/<str:pk>/', update_users_admin, name='update_users_admin'),
    # USUARIOS ESTUDIANTES
    path('student/list/debt/', list_students_debt, name='list_students_debt'), #listado de estudiantes por meses en mora - estadisticas
    path('student/list/debt/app/', list_students_debt_app, name='list_students_debt_app'), #listado de estudiantes por meses en mora - APP estadisticas
    path('student/list/<str:grade>/<str:schedule>/', list_students_grades, name='list_students_grades'), #listado de estudiantes filtrado por grado y jornada
    path('student/get/<str:pk>/', get_student_full, name='get_student_full'),
    path('student/list/', list_students, name='list_students'),#necesita un listado que se carga al inicio
    path('student/create/', create_students, name='create_students'),
    path('student/update/<str:pk>/', update_students, name='update_students')
]
