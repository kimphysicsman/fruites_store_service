from rest_framework import serializers

from user.models import User as Usermodel

class UserSerializer(serializers.ModelSerializer):
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)
        instance.save()

        return instance


    class Meta:
        model = Usermodel
        fields = ["id", "username", "type", "password", "is_active"
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }

