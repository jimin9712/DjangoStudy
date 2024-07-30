from django.urls import path
from user import views
urlpatterns = [
    path('list/', views.list), # user/list/ => views.py의 list 함수가 처리..

    path('delete/',views.delete),

    path('detail/<int:id>/',views.detail),

    path('create/',views.create),

    path('ex01/',views.func01), # template 사용. render 함수

    path('ex02/',views.func02), # context 값, 주석

    path('ex03/',views.func03), #dot-lookup

    path('ex04/',views.func04), #if, for

]
