from rest_framework.views import APIView
from rest_framework.response import Response
from assets.serializers import HostSerializer
from assets.models import Host
from assets.forms import HostForm
from opsrobot.view import DocParam



class HostViewSet(APIView):

    coreapi_fields = (
        DocParam(name="hostname", location='form', description='主机名'),
        DocParam(name="ip_addr", location='form', description='ip'),
    )

    def post(self,request):
        form_obj = HostForm(request.data)
        if form_obj.is_valid():
            form_obj.save()
        serializer_class = HostSerializer(Host.objects.all(),many=True)
        return Response(serializer_class.data)

class ShowHostViewSet(APIView):
    def get(self,request):
        """
        all hosts
        """
        host = Host.objects.all()
        serializer_class = HostSerializer(host,many=True)
        return Response(serializer_class.data)

class HostView(APIView):

    def delete(self,request,host_name):
        Host.objects.filter(hostname=host_name).delete()
        serializer_class = HostSerializer(Host.objects.all(), many=True)
        return Response(serializer_class.data)

    def put(self,request,host_name):
        return Response(host_name)


