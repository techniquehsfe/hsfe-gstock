from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from gStock.views import index

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        userToken = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=userToken)

        if userToken:
            user = authenticate(username=request.data['username'], password=request.data['password'])
            if user:
                login(request, user)

        return Response({
            'token': token.key,
            'user': userToken.pk, # Ici c'est l'ID de l'user qui est envoyé au frontend
            'current_username': userToken.username,
            # 'data': request.data # just to know receiving data
        })


class LogoutView(TemplateView):

  def get(self, request, **kwargs):

    logout(request)

    return redirect(index)
