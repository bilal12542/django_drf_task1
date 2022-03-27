from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

posts_router = DefaultRouter()
posts_router.register('', views.PostCRUD, basename='post')

urlpatterns = [
    path('', include(posts_router.urls)),
    # path('<int:pk>/', include(user_router.urls))
]
