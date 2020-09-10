from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    email_destination = serializers.EmailField()
    content = serializers.CharField(max_length=500)

class SmsSerializer(serializers.Serializer):
    phone_to = serializers.CharField(max_length=15) 
    sms = serializers.CharField(max_length=500)