
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
import json
from django.http import JsonResponse
from backend.models import Book
from django.core import serializers
# Create your views here.
import traceback

def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['code'] = 20000
    except  Exception as e:
        response['msg'] = request.GET
        response['code'] = 50004

    return JsonResponse(response)

def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['code'] = 20000
    except  Exception as e:
        traceback.print_exc(e)
        response['msg'] = str(e)
        response['code'] = 50004

    return JsonResponse(response)