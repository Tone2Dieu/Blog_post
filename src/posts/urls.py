from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

#Create path url

router = SimpleRouter()

router.register('users', views.UserViewSet, basename='users')
router.register('', views.PostViewSet, basename='posts')


urlpatterns = router.urls