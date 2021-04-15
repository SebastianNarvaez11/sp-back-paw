from rest_framework import serializers
from .models import Payment, CompromisePay
from users.models import User, Student
from school.models import Grade


class PaymentSerializer(serializers.ModelSerializer):
    create = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'value', 'description',
                  'student', 'reference', 'method', 'create']
############################################################################
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    grade = GradeSerializer()
    class Meta:
        model = Student
        fields = ['id' , 'user', 'grade']


class PaymentWhiteStudentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    create = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related('student')
        return queryset

    class Meta:
        model = Payment
        fields = ['id', 'value', 'description',
                  'student', 'reference', 'method', 'create']

############################################################################


class CompromiseSerializer(serializers.ModelSerializer):
    create = serializers.DateTimeField(
        format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = CompromisePay
        fields = ['id', 'person_charge', 'document', 'month_owed',
                  'value', 'student', 'date_pay', 'state', 'create']


############################################################################

class CompromiseWithStudentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    create = serializers.DateTimeField(
        format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = CompromisePay
        fields = ['id', 'person_charge', 'document', 'month_owed',
                  'value', 'student', 'date_pay', 'state', 'create']