from django.contrib.auth import get_user_model
from rest_framework import serializers
from topics.models import Topic, Message

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = ('id', 'register_date', 'is_admin', 'is_active', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = UserModel(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'
        read_only_fields = ('id', 'create_date', 'slug', 'author')
