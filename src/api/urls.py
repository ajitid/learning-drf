from django.urls import path, include
from rest_framework import routers

from . import views

# router = routers.DefaultRouter(trailing_slash=False)
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('screens', views.ScreenViewSet)


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls), name='api'),
    path('screens/<str:screen_name>/<str:seat_name>',
         views.seat_view, name='seat-detail'),
]
