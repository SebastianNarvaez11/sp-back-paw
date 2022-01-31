from rest_framework import serializers
from .models import Grade
# from users.serializers import UserSerializer


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'name', 'abbreviation',
                  'enrollment', 'monthly_pay', 'deleted']

# serializador que pasa el valor total que an pagado


class GradeAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'name', 'abbreviation', 'enrollment',
                  'monthly_pay', 'deleted', 'total_raised']

# serializer para los reportes, solo con el nombre
class GradeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['name', 'enrollment', 'monthly_pay']