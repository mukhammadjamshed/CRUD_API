from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets
from rest_framework.generics import UpdateAPIView




# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# this a APIView fuction , we can use with all other views
class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f'Returned {len(books)} books',
            "books": serializer_data
        }

        return Response(data)


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiVIew(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# new added ViewSet to use CRUD operations
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
