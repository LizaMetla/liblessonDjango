from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_null=False)
