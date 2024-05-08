"""
URL configuration for start_pyt18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from biblioteczka import views
urlpatterns = [
    path("", views.index, name="index"),
    path("index2/", views.index2, name="index2"),
    path('next/', views.next, name="next"),
    path('cars/', views.cars, name="cars"),
    path('add_car/', views.add_car, name="add_car"),
    path('add_author/', views.add_author, name="add_author"),
    path('delete_author/<int:pk>/', views.delete_author, name="delete_author"),
    path('add_publisher/', views.add_publisher, name="add_publisher"),
    path('authors/', views.authors_list, name="authors_list"),
    path('publishers/', views.publishers_list, name="publishers_list"),
    path('author/<int:pk>', views.detail_author, name="detail_author"),
    path('del_car/<int:a>/', views.del_car, name="del_car"),
    path('add_book/', views.add_book, name="add_book"),
    path('add_genre/', views.add_genre, name="add_genre"),
    path('cars/<int:a>/', views.mycar, name="mycar"),
    path('books/', views.book_list, name="book_list"),
    path('update_book/<int:pk>', views.update_book, name="update_book"),
    path('genre/', views.genre_list, name="genre_list"),
    path('liczba/', views.losuj, name="losuj"),
    path('dod/<int:a>/<int:b>/', views.dodawanie, name="dodawanie"),
    path('odj/<int:a>/<int:b>/', views.odejmowanie, name="odejmowanie"),
    path('mno/<int:a>/<int:b>/', views.mnozenie, name="mnozenie"),
    path('dzi/<int:a>/<int:b>/', views.dzielenie, name="dzielenie"),
    path('tab/<int:a>/<int:b>/', views.tabliczka, name="tabliczka"),
    path('losuj/<int:a>/<int:b>/<int:ilosc>/', views.losuj2, name="losuj2"),
    path('admin/', admin.site.urls),
]
