"""hw1_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from hw1app.views import index, archive, user_identification, users, article_num

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('articles/', include('hw1app.urls')),
    path('articles/<int:article_number>/', article_num, name="article_number"),
    path('articles/<int:article_number>/archive/', archive, name="archive"),
    path('users/', users, name="users"),
    path('users/<int:user_id>/', user_identification, name="users_id"),

]


