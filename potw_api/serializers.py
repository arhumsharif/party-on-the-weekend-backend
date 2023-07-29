from rest_framework import serializers
from .models import Place, User

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class PlaceRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    genres = serializers.ListField(child=serializers.CharField())
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    credentials = serializers.CharField()
    radius = serializers.FloatField()

class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    genres = serializers.ListField(child = serializers.CharField())
    credentials = serializers.CharField()

    def create(self, validated_data):
        # Create and return a new User instance using the validated data
        return User.objects.create(**validated_data)