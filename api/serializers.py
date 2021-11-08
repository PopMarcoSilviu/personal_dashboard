from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        dictionary = {'first_name': validated_data['first_name'],
                      'last_name': validated_data['last_name'], }
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'],
                                        **dictionary)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]
