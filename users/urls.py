from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

user_router = DefaultRouter()
user_router.register('', views.ProfileApiView, basename='user')

urlpatterns = [
    # path('login/', views.login_user, name='login'),
    path('', include(user_router.urls))
]
