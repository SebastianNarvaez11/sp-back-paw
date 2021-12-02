from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdminSerializer, UserSerializer, UserUpdateSerializer, StudentSerializer, UserStudentFilterSerializer, UserGradeFilterSerializer, UserStudentDebtSerializer, UserStudentDebtAppSerializer, UserStudentReportSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Admin, User, Student


# Create your views here.

# CON ESTA VISTA ESTAMOS OBTENIENDO EL USUARIO ACTUAL COMO OBJETO
# NO TIENE NADA QUE VER CON EL USUARIO QUE SE DEVUELVE JUNTO AL TOKEN AL INICIAR SECCION
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

# CON ESTA VISTA ESTAMOS LISTANDO LOS USERS GENERALES
# VISTA PARA HACER ALGUN QUERYSET PERSONALIZADO AL LISTAR LOS USUARIOS
# EN LAS VISTA DE USUARIOS ES NECESIOR EXCLUIR LOS USUARIOS ELIMINADOS MANUALMENTE,
# YA QUE AL HEREDAR PRIMERO LA CLASE BASE Y LUEGO ABSTRAPUSER GENERA UN COMFLICTO
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_users(request):
    users = User.objects.exclude(deleted=True).exclude(id=request.user.id).exclude(admin=None).exclude(type=3).exclude(is_superuser=True)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# CON ESTA VISTA ESTAMOS ACTUALIZANDO LOS USUARIOS GENERALES
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_users(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserUpdateSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CON ESTA VISTA ESTAMOS ELIMINANDO LOS USUARIOS GENERALES
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_users(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# CON ESTA VISTA ESTAMOS CREANDO LOS USUARIOS ADMIN
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_users_admin(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CON ESTA VISTA ESTAMOS ACTUALIZANDO LOS USUARIOS ADMIN
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_users_admin(request, pk):
    admin = Admin.objects.get(pk=pk)
    serializer = AdminSerializer(admin, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CON ESTA VISTA ESTAMOS LISTANDO TODOS LOS USERS ESTUDIANTES AL INICIO PARA TENERLOS LISTOS PARA FILTRAR
# VISTA PARA HACER ALGUN QUERYSET PERSONALIZADO AL LISTAR SOLO LOS ESTUDIANTES
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_students(request):
    users = User.objects.select_related().exclude(deleted=True).exclude(type=1).exclude(type=2).exclude(student__grade=None)
    serializer = UserStudentFilterSerializer(users, many=True)
    return Response(serializer.data)


# CON ESTA VISTA ESTAMOS LISTANDO LOS USERS ESTUDIANTES POR GRADO Y JORNADA
# VISTA PARA HACER ALGUN QUERYSET PERSONALIZADO AL LISTAR SOLO LOS ESTUDIANTES
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_students_grades(request, grade, schedule):
    users = User.objects.exclude(deleted=True).filter(
        student__grade__id=grade).filter(student__schedule=schedule)
    serializer = UserGradeFilterSerializer(users, many=True)
    return Response(serializer.data)
#####################################################################################################################################################################
# CON ESTA VISTA ESTAMOS LISTANDO LOS USERS ESTUDIANTES POR CANTIDAD DE MESES EN MORA PARA ESTADISTICAS
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_students_debt(request):
    users = User.objects.select_related().exclude(deleted=True).exclude(type=1).exclude(type=2).exclude(student__grade=None).exclude(student__coverage=True)
    serializer = UserStudentDebtSerializer(users, many=True)
    return Response(serializer.data)


# CON ESTA VISTA ESTAMOS LISTANDO LOS USERS ESTUDIANTES POR CANTIDAD DE MESES EN MORA PARA ESTADISTICAS DE LA APP
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_students_debt_app(request):
    users = User.objects.select_related().exclude(deleted=True).exclude(type=1).exclude(type=2).exclude(student__grade=None).exclude(student__coverage=True)
    serializer = UserStudentDebtAppSerializer(users, many=True)
    return Response(serializer.data)


# CON ESTA VISTA ESTAMOS LISTANDO LOS USERS ESTUDIANTES POR CANTIDAD DE MESES PARA LOS REPORTES
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_students_report(request):
    users = User.objects.select_related().exclude(type=1).exclude(type=2).exclude(student__grade=None)
    serializer = UserStudentReportSerializer(users, many=True)
    return Response(serializer.data)

#####################################################################################################################################################################

# CON ESTA VISTA ESTAMOS CREANDO LOS ESTUDIANTES
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_students(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CON ESTA VISTA ESTAMOS ACTUALIZANDO LOS ESTUDIANTES
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_students(request, pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# CON ESTA VISTA ESTAMOS OBTENIENDO EL ESTUDIANTE COMPLETO CON PAGOS COMO OBJETO
# NO TIENE NADA QUE VER CON EL USUARIO QUE SE DEVUELVE JUNTO AL TOKEN AL INICIAR SECCION
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_student_full(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
