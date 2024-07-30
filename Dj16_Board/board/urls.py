from django.urls import path
from board import views

urlpatterns = [
    path('list/', views.list), # board/list => views.py의 list()가 처리
    path('write/', views.write),
    path('detail/<int:id>/', views.detail),
    path('update/', views.update),
    path('update/<int:id>/', views.update),
    path('delete/', views.delete),
    

]
