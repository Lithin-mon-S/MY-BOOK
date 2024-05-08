from django.urls import path
from . import views

urlpatterns = [
    path('', views.listBook, name='booklist'),
    path('create_book', views.creatbook, name='createbook'),
    path('author/', views.Create_Author, name='author'),
    path('detailviews/<int:book_id>/', views.detailviews, name='Details'),
    path('updateview/<int:book_id>/', views.updatebook, name='upadet'),
    path('Deleteview/<int:book_id>/', views.Deleteview, name='Delete'),
    path('index/', views.index),
    path('search/', views.Search_Book, name='search'),

]
