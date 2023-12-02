from rest_framework import serializers
from django.contrib.auth.models import User

MIN_LENGTH = 8

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {"min_length": "Password does not match"}
    )
    password2 = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {"min_length": "Password does not match"}
    )
    email = serializers.EmailField(label="Email Address")

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
    
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
    