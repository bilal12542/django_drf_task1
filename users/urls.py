from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

user_router = DefaultRouter()
user_router.register('users', views.ProfileApiView, basename='users')

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.login_user, name='login'),
    path('', include(user_router.urls)),
    # path('<int:pk>/', include(user_router.urls))
]
