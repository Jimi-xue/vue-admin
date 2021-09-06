import json

from rest_framework.views import APIView
from rest_framework.response import Response
from backend.views.serializers import BookSerializer
from backend.models import Book
from backend.forms import BookForm
from vueproject.view import DocParam



class BookViewSet(APIView):

    coreapi_fields = (
        DocParam(name="book_name", location='form', description='书名'),
    )

    def post(self,request):
        form_obj = BookForm(request.data)
        if form_obj.is_valid():
            form_obj.save()
        serializer_class = BookSerializer(Book.objects.all(),many=True)
        return Response(serializer_class.data)

class ShowBooksViewSet(APIView):
    def get(self,request):
        """
        all books
        """
        book = Book.objects.all()
        serializer_class = BookSerializer(book,many=True)
        return Response(serializer_class.data)

class BookView(APIView):

    def delete(self,request,book_name):
        Book.objects.filter(book_name=book_name).delete()
        serializer_class = BookSerializer(Book.objects.all(), many=True)
        return Response(serializer_class.data)

    def put(self,request,book_name):
        return Response(book_name)
