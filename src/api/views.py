from django.contrib.auth.models import User
from rest_framework import viewsets, response, generics, views

from screens.models import Screen, Seat

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserLimitedFieldsSerializer
        else:
            return serializers.UserSerializer

    # def get(self, request):

# class ScreenViewSet(viewsets.ViewSet):
#     queryset = Screen.objects.all()
#     serializer_class = ScreenSeatSerializer

#     def list(self, request):
#         res = []
#         for screen in Screen.objects.all():
#             screen_info = {'name': screen.name, 'seat_info': {}}
#             for seat in screen.seat_set.all():
#                 screen_info['seat_info'][seat.name] = {
#                     'count': seat.count,
#                     'aisle': seat.aisle,
#                     'reserved': seat.reserved,
#                 }
#             res.append(screen_info)
#         return response.Response(res)

#     def create(self, request):
#         data = request.data
#         screen = Screen.objects.get_or_create(name=data['name'])[0]
#         for seat_name in data['seat_info'].keys():
#             Seat.objects.create(
#                 screen=screen,
#                 name=seat_name,
#                 count=data['seat_info'][seat_name]['count'],
#                 aisle=data['seat_info'][seat_name]['aisle'],
#                 reserved=[]
#             )


# class ReserveSeatsView(views.APIView):
#     queryset = Screen.objects.all()

#     def post(self, request):
#         screen_name = self.kwargs['screen_name']
#         print(screen_name)
