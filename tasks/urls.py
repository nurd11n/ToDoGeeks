from django.urls import path, include
from .views import TaskModelView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('tasks', TaskModelView, basename='order')


urlpatterns = [
    path('', include(router.urls)),
]