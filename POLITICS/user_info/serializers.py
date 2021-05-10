from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework import status


class CreateUserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        print(username,password)

        user_1 = User.objects.filter(username=username, password=password)
        print(user_1.values())

        if username and password:
            # it checks username, password in database if available, return user object
            try:
                user = User.objects.get(username=username, password=password)
            except Exception as e:
                raise NotFound

            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError("User Not Activated")
            else:
                raise serializers.ValidationError("Unable to login")
        else:
            raise ValidationError("Username and Password are required", status.HTTP_400_BAD_REQUEST)

        return data