from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
# router.register('screens', ScreenViewSet)
# router.register('sc', ReserveSeatsView)
# router.register(r'^screens/{screen_name}/reserve$', ReserveSeatsView)


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),

]
