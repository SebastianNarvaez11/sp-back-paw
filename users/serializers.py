from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from base.validators import *
from .models import Admin, User, Student
from school.serializers import GradeSerializer
from payment.serializers import PaymentSerializer, CompromiseSerializer
# serializer para crear y actualizar los admin ya que resiven solo el id y no el objeto completo
# el password no es requerido para la actualizacion


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'user', 'position']

################################################################################################################################################################
# serializer para obtener las datos basicos al inicio para poder filtrar por estudiante


class StudentListFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'code']

# serializer para obtener las datos basicos al inicio para poder filtrar por estudiante


class UserStudentFilterSerializer(serializers.ModelSerializer):
    student = StudentListFilterSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'student']
        extra_kwargs = {
            'student': {'required': False}
        }


################################################################################################################################################################
#ESTADISTICAS
# serializer para obtener los todos estudiantes para el envio masivo de emails y sms, filtrados solo por el numero de meses en mora

class StudentDebtSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()

    class Meta:
        model = Student
        fields = ['id', 'user', 'code', 'grade',
                  'schedule', 'monthOwed', 'amountOwed']


class UserStudentDebtSerializer(serializers.ModelSerializer):
    student = StudentDebtSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'student']
        extra_kwargs = {
            'student': {'required': False}
        }

###### APP

class StudentDebtAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'schedule', 'monthOwed', 'amountOwed']


class UserStudentDebtAppSerializer(serializers.ModelSerializer):
    student = StudentDebtAppSerializer()

    class Meta:
        model = User
        fields = ['id', 'student']
        extra_kwargs = {
            'student': {'required': False}
        }

################################################################################################################################################################
# serializer para obtener el listado filtrado por grados de estudiantes sin  los pagos


class StudentGradeFilterSerializer(serializers.ModelSerializer):
    total_year = serializers.IntegerField(read_only=True)
    total_paid = serializers.IntegerField(read_only=True)
    monthly_payment = serializers.IntegerField(read_only=True)
    monthOwed = serializers.IntegerField(read_only=True)
    amountOwed = serializers.IntegerField(read_only=True)
    grade = GradeSerializer()
    payments = PaymentSerializer(many=True, read_only=True)
    compromises = CompromiseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'code', 'grade', 'phone1', 'phone2', 'document_type', 'document',
                  'attending', 'discount', 'initial_charge', 'coverage',
                  'schedule', 'total_year', 'total_paid', 'monthly_payment', 'monthOwed', 'amountOwed', 'payments', 'compromises']

# serializer para obtener el listado filtrado de estudiantes sin los pagos


class UserGradeFilterSerializer(serializers.ModelSerializer):
    student = StudentGradeFilterSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'student']
        extra_kwargs = {
            'student': {'required': False}
        }
################################################################################################################################################################

# serializer para obtener los students individualmente ya que necesitamos el grado como objeto
# el password no es requerido para la actualizacion


class StudentGetSerializer(serializers.ModelSerializer):
    total_year = serializers.IntegerField(read_only=True)
    total_paid = serializers.IntegerField(read_only=True)
    monthly_payment = serializers.IntegerField(read_only=True)
    monthOwed = serializers.IntegerField(read_only=True)
    amountOwed = serializers.IntegerField(read_only=True)
    grade = GradeSerializer()
    payments = PaymentSerializer(many=True, read_only=True)
    compromises = CompromiseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'grade', 'code', 'phone1', 'phone2', 'document_type', 'document',
                  'attending', 'discount', 'initial_charge', 'coverage',
                  'schedule', 'total_year', 'total_paid', 'monthly_payment', 'monthOwed', 'amountOwed', 'payments', 'compromises']


# serializer para CREAR Y ACTUALIZAR los students ya que se necesita solo el id del grado y usuario para relacionarlo
# el password no es requerido para la actualizacion
class StudentSerializer(serializers.ModelSerializer):
    total_year = serializers.IntegerField(read_only=True)
    total_paid = serializers.IntegerField(read_only=True)
    monthly_payment = serializers.IntegerField(read_only=True)
    monthOwed = serializers.IntegerField(read_only=True)
    amountOwed = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'grade', 'document_type', 'document', 'code', 'phone1', 'phone2',
                  'attending', 'discount', 'initial_charge', 'coverage', 'schedule',
                  'total_year', 'total_paid', 'monthly_payment', 'monthOwed', 'amountOwed']


# SERIALIZER PARA OBTENER USUARIOS AL INICIAR SECCION PARA QUE
# CADA USUARIO TENGA SU PERFIL EN FORMA DE OBJETO
# tiene relacion con la configuracion que necesita el serializador del token
class UserSerializer(serializers.ModelSerializer):
    admin = AdminSerializer()
    student = StudentGetSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'type',
                  'first_name', 'last_name', 'is_active', 'deleted', 'admin', 'student']

        extra_kwargs = {
            'admin': {'required': False},
            'student': {'required': False}
        }


# SERIALIZER PARA ACTUALIZAR USUARIOS GENERALES
# YA QUE PARA ACTUALIZAR UN USUARIO NO ES NECESARIO PASAR SU PERFIL
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'type',
                  'first_name', 'last_name', 'is_active', 'deleted']


# SERIALIZER PARA EL REGISTRO DE USUARIOS CON CAMPOS ADICIONALES
# tambien se debe hacer referencia en el settings
class MyRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(
        required=True, write_only=True, validators=[validate_only_letters])
    last_name = serializers.CharField(
        required=True, write_only=True, validators=[validate_only_letters])
    type = serializers.IntegerField(max_value=4, min_value=1, required=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'type': self.validated_data.get('type', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        # remplazar los campos personalizados antes de guardar
        user.type = self.cleaned_data.get('type')
        # guardar la instancia de usuario
        user.save()
        return user
