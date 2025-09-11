"""
URL configuration for indie_projects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'devlog'

urlpatterns = [
    path('', views.devlog_home, name='devlog_home'),
    path('category/<slug:cat_slug>/', views.devlog_home, name='post-by-category'),
    path('author/<str:author_username>/', views.devlog_home, name='post-by-author'),
    path('search/', views.devlog_search, name='search'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]
