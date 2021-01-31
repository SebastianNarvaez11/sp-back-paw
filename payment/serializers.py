from rest_framework import serializers
from .models import Payment, CompromisePay
from users.models import User, Student


class PaymentSerializer(serializers.ModelSerializer):
    create = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'value', 'description',
                  'student', 'reference', 'method', 'create']
# ###########################################################################


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = ['user']


class PaymentWhiteStudentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    create = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

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
