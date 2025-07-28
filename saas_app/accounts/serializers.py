from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import authenticate
from . models import Account
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    subscription_plan = serializers.ChoiceField(choices=Account.PLAN_CHOICES)
    plan_info = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'subscription_plan', 'plan_info']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        
        Account.objects.create(
            user=user,
            subscription_plan=validated_data['subscription_plan'],
            plan_info=validated_data['plan_info'] if 'plan_info' in validated_data else '',
        )
        return user 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            data['user'] = user
            return data
        raise serializers.ValidationError("Invalid credentials")
    