from rest_framework import serializers
from .models import User, Team

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'age', 'nationality', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        # when retrieving user data through the API, 
        # the password field won't be exposed in the response.

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name', 'gender', 'captain', 'players_info']
        read_only_fields = ['captain']