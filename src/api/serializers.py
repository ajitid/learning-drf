from rest_framework import serializers
from django.contrib.auth.models import User

from screens.models import Screen, Seat


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
        }


class UserLimitedFieldsSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('url', 'username')


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ("name", "count", "aisle", "reserved",)


class ScreenSerializer(serializers.HyperlinkedModelSerializer):
    seats = serializers.SerializerMethodField()

    class Meta:
        model = Screen
        fields = ('name', 'seats')

    def get_seats(self, obj):
        data = SeatSerializer(obj.seats.all(), many=True).data
        return data


class ScreenLimitedFieldsSerializer(ScreenSerializer):
    class Meta(ScreenSerializer.Meta):
        fields = ('url', 'name',)

# class ScreenSeatSerializer(serializers.Serializer):
#     seat_info = serializers.JSONField()

#     class Meta:
#         model = Screen
#         fields = ('name')
