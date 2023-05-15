from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView, BookDetailApiView, \
    BookUpdateApiView, BookDeleteApiView, BookCreateApiVIew, \
    BookListCreateApiView, BookListUpdateDeleteApiView, BookViewSet

# if you wanna , you can use this CRUD operations
router = SimpleRouter()
router.register('books', BookViewSet, basename='books')


# otherwise , you can use this views' urls

urlpatterns = [
    # path('books/', BookListApiView.as_view()),
    # path('booklistcreate/', BookListCreateApiView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookListUpdateDeleteApiView.as_view()),
    # path('books/create/', BookCreateApiVIew.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
]


urlpatterns = urlpatterns + router.urls