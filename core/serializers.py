from core.models import User, Chryon
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class ChryonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chryon
        fields = [
            'pk',
            'date',
            'city',
            'state',
            'description',
        ]

