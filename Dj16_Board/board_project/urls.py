"""board_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect
urlpatterns = [
    path("admin/", admin.site.urls),
     # board/...  으로 요청이 들어오면,  board 앱의 urls.py 로 처리 위임
    path('board/', include('board.urls')),

   # empty path 를 redirect 하기
    path('',lambda request: redirect('/board/list/'))

]


