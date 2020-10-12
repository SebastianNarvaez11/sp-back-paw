from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializer, SmsSerializer, WppSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.mail import EmailMessage
from twilio.rest import Client
from users.models import User

# Create your views here.
# Credenciales para el envio de sms Twilio
account_sid = 'ACaaf5d8fb4c1df5e8ea2a9f75ea2701f3'
auth_token = 'ac9425d85a5055a17fe3d98f34d4844e'

# Vista para enviar sms individualmente
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_sms(request):
    serializer = SmsSerializer(data=request.data)
    if serializer.is_valid():
        sms = request.data['sms']
        phone_to = request.data['phone_to']
        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                body=sms,
                from_='+14702643943',
                to=phone_to
            )
            print(message.sid)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        print(message.sid)


# Vista para enviar sms masivos
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_sms_massive(request):
    serializer = SmsSerializer(data=request.data, many=True)
    if serializer.is_valid():
        not_sent = []
        sent = 0
        for message in request.data:
            sms = message['sms']
            phone_to = message['phone_to']
            client = Client(account_sid, auth_token)

            try:
                message = client.messages.create(
                    body=sms,
                    from_='+14702643943',
                    to=phone_to
                )
                sent = sent + 1
                print(message.sid)

            except:
                not_sent.append(message['user'])

        print('sms no enviados:', not_sent)
        data = {'sent': sent, 'not_sent': not_sent}
        return Response(data, status=status.HTTP_200_OK)


# vista para enviar correos
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_email(request):
    # Optiene los datos del formulario
    serializer = EmailSerializer(data=request.data)
    if serializer.is_valid():
        email_destination = request.data['email_destination']
        content = request.data['content']

        # ENVIAMOS EL CORREO
        email = EmailMessage(
            "Colegio Ejemplo - Circular Financiera",  # Asunto del mensaje
            "Remitente: {} \nEmail: <{}> \n\nEscribio: \n\n{} ".format(
                'Colegio Ejemplo', 'colegio@gmail.com', content),  # estructura del mensaje
            "testing.developer.404@gmail.com",  # email de origen
            [str(email_destination)],  # email de destino
            reply_to=[email_destination]
        )
        try:
            email.send()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vista para enviar correos masivos
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_email_massive(request):
    serializer = EmailSerializer(data=request.data, many=True)
    if serializer.is_valid():
        not_sent = []
        sent = 0
        for correo in request.data:
            email_destination = correo['email_destination']
            content = correo['content']

            email = EmailMessage(
                "Colegio Ejemplo - Circular Financiera",  # Asunto del mensaje
                "Remitente: {} \nEmail: <{}> \n\nEscribio: \n\n{} ".format(
                    'Colegio Ejemplo', 'colegio@gmail.com', content),  # estructura del mensaje
                "testing.developer.404@gmail.com",  # email de origen
                [str(email_destination)],  # email de destino
                reply_to=[email_destination]
            )

            try:
                email.send()
                sent = sent + 1

            except:
                not_sent.append(correo['user'])

        print('correos no enviados:', not_sent)
        data = {'sent': sent, 'not_sent': not_sent}
        return Response(data, status=status.HTTP_200_OK)


# Vista para enviar Wpp individualmente
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_wpp(request):
    serializer = WppSerializer(data=request.data)
    if serializer.is_valid():
        sms = request.data['sms']
        phone_to = request.data['phone_to']
        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                body=sms,
                from_='whatsapp:+14155238886',
                to='whatsapp:+573188524067'
            )
            print(message.sid)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        print(message.sid)