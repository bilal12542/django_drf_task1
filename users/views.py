from django.shortcuts import render
from .form import CustomUserForm
from .models import MyUser
from django.views.generic import CreateView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .permissions import IsUserOrReadOnly


class ProfileApiView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def list(self, request):
        users = MyUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = MyUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = MyUser.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class SignUpView(CreateView):
    model = MyUser
    form_class = CustomUserForm
    success_url = 'login'
    template_name = 'signup.html'


def login_user(request):
    logout(request)
    try:
        if request.POST:
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')

        return render(request, 'login.html')
    except Exception as e:
        print(e)
