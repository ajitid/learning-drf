from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from screens.models import Screen, Seat

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # filter_backends = (,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserLimitedFieldsSerializer
        else:
            return serializers.UserSerializer


class ScreenViewSet(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    # serializer_class = serializers.ScreenSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ScreenLimitedFieldsSerializer
        else:
            return serializers.ScreenSerializer


@api_view()  # by default get
# @renderer_classes((JSONRenderer,)) # by default api_view gives JSON and html renderer
def seat_view(request, screen_name, seat_name):
    seat = Seat.objects.filter(
        name=seat_name, screen__name=screen_name).first()
    if seat is None:
        return Response(status=404)
    data = serializers.SeatSerializer(seat).data
    return Response(data)


class SeatView(APIView):
    def get(self, request, seat_name, screen_name):
        seat = Seat.objects.filter(
            name=seat_name, screen__name=screen_name).first()
        if seat is None:
            return Response(status=404)
        data = serializers.SeatSerializer(seat).data
        return Response(data)
