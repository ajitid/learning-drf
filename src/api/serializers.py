from rest_framework import serializers
from django.contrib.auth.models import User

from screens.models import Screen


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserLimitedFieldsSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('url', 'username')


# class ScreenSeatSerializer(serializers.Serializer):
#     seat_info = serializers.JSONField()

#     class Meta:
#         model = Screen
#         fields = ('name')


# class ScreenSerializer(serializers.Serializer):
#     class Meta:
#         model = Screen
#         fields = ('name')
