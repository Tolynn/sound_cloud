from rest_framework import  serializers


class GoogleAuth(serializers.Serializer):
    """сериализация данных от гугл
    """
    email=serializers.EmailField()
    token=serializers.CharField()
