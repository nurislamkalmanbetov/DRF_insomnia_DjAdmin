from django.contrib import admin
from django.urls import path, include
from posts.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('',PostViewset,basename='posts')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('posts/', include(router.urls)), 
    path('auth/', include('accounts.urls')),
]
