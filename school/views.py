from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import GradeSerializer, GradeAlterSerializer
from .models import Grade

# Create your views here.
class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeAlterSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]