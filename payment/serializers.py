from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    create = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Payment
        fields = ['id','value', 'description', 'student', 'reference', 'method', 'create']