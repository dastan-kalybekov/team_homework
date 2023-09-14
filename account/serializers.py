from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'telegram_chat_id']
<<<<<<< HEAD
=======
    #
    # def validate_password(self, attrs):
    #     if len(attrs['password']) < 10:
    #         raise serializers.ValidationError('длина пароля должна быть не менее 10 символов')
    #     if not any(c.isdigit()
    #                for c in attrs['password']):
    #         raise serializers.ValidationError('пароль должен содержать минимум 1 цифру')
    #     if not any(c.isalpha()
    #                for c in attrs['password']):
    #         raise serializers.ValidationError('пароль должен содержать минимум 1 букву')
    #     return attrs
>>>>>>> 3cecb1452812b2c240346eaee15d8f4353ee47f0

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            telegram_chat_id=validated_data['telegram_chat_id']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
<<<<<<< HEAD
=======

>>>>>>> 3cecb1452812b2c240346eaee15d8f4353ee47f0
