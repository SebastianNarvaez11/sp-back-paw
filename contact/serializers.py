from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    email_destination = serializers.EmailField()
    content = serializers.CharField(max_length=500)