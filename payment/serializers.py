from rest_framework import serializers
from .models import Payment
from users.serializers import StudentGetSerializer

class PaymentGetSerializer(serializers.ModelSerializer):
    create = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    student = StudentGetSerializer()
    class Meta:
        model = Payment
        fields = ['id','value', 'description', 'reference', 'method', 'student', 'create']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','value', 'description', 'student', 'reference', 'method']