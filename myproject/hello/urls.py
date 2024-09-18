from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello_world.as_view(), name='hello_world'),
    path('author/',views.author_form.as_view(), name='author_form'),
    path('review/',views.ReviewView.as_view(), name='review_form'),
    path('review/<int:pk>',views.ReviewEditView.as_view(), name='review_form'),
    path('book/',views.BookListView.as_view(), name='book_form'),
    path('book/<int:pk>',views.BookDetailView.as_view(), name='book_form'),
]
