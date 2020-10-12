from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    user = serializers.CharField()
    email_destination = serializers.EmailField()
    content = serializers.CharField(max_length=900)


class SmsSerializer(serializers.Serializer):
    user = serializers.CharField()
    phone_to = serializers.CharField(max_length=15)
    sms = serializers.CharField(max_length=500)

class WppSerializer(serializers.Serializer):
    user = serializers.CharField()
    phone_to = serializers.CharField(max_length=15)
    sms = serializers.CharField(max_length=500)