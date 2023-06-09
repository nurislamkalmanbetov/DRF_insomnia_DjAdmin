from . import views
from django.urls import path


urlpatterns = [
    path('homepage/', views.homepage, name="posts_home"),
    path('', views.PostListCreateView.as_view(), name="list_posts"),
    path('<int:pk>/', views.PostRetriveUpdateDeleteView.as_view(), name="post_detail"),
    path('current_user/', views.get_posts_for_current_user, name="current_user"),
]


# djaneiro