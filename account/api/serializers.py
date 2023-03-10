from rest_framework import serializers
from account import models as account_models

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = account_models.User
        fields = ["email","password"]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user