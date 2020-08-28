from rest_framework import serializers
from .models import Grade
# from users.serializers import UserSerializer


class GradeSerializer(serializers.ModelSerializer):
    # students = serializers.StringRelatedField(many=True, read_only=True)#da un listado de estudiantes que pertenecen a este grado
    class Meta:
        model = Grade
        fields = ['id', 'name', 'enrollment','monthly_pay', 'deleted']
    

