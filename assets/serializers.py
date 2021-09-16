from assets.models import Host
from rest_framework import serializers
from django.contrib.auth.models import User

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('id','hostname','ip_addr',"remark","asset_id","add_time" )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','is_superuser')