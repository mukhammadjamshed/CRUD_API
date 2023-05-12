from django.urls import path
from .views import BookListApiView, BookDetailApiView, \
    BookUpdateApiView, BookDeleteApiView, BookCreateApiVIew, \
    BookListCreateApiView, BookListUpdateDeleteApiView

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('booklistcreate/', BookListCreateApiView.as_view()),
    path('bookupdatedelete/<int:pk>/', BookListUpdateDeleteApiView.as_view()),
    path('books/create/', BookCreateApiVIew.as_view()),
    path('books/<int:pk>/', BookDetailApiView.as_view()),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
]