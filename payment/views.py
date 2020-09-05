from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Payment

# CON ESTA VISTA ESTAMOS OBTENIENDO LOS PAGOS POR ESTUDIANTE
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_payments_for_students(request, pk):
    pays = Payment.objects.filter(student__id=pk)
    print(pays)
    serializer = PaymentSerializer(pays, many=True)
    return Response(serializer.data)


# CON ESTA VISTA ESTAMOS CREANDO LOS DESDE PAYU
@api_view(['POST'])
def create_payment(request):
    print(request.data)
    rq_data = request.data.dict()
    if rq_data['state_pol'] == '4':
        data = {'value': rq_data['value'],
                'reference': rq_data['reference_pol'],
                'method': rq_data['payment_method_name'],
                'description': rq_data['description'],
                'student': rq_data['extra1']}
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vista para la creacion de pagos manuales
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_payment_manual(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)