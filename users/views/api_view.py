# -*- coding: utf-8 -*-
import json
import os
import time

from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from users.forms import UserForm
from opsrobot.settings import MEDIA_ROOT

class UserView(APIView):

    def get(self,request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data)

    def put(self,request):
        form_obj = UserForm(request.data)
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        print(form_obj.is_valid())
        if form_obj.is_valid():
            user.__dict__.update(form_obj.cleaned_data)
            user.save()
            return Response(200)
        else:
            return  Response(form_obj.errors)

class UserAvatar(APIView):

    def post(self,request):
        file = request.FILES.get("avatar")
        user_id = request.user.id
        now_tm = str(time.time())
        user = User.objects.get(id=user_id)
        avatar = user.username + now_tm
        file_path = MEDIA_ROOT
        local_file = os.path.join(file_path,user.username + now_tm)
        with open(local_file,'wb') as f:
            for line in file.chunks():
                f.write(line)
        user.avatar = avatar
        user.save()
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data)


