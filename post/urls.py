from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostListCreateApiView.as_view()),
    path('post/<int:pk>/', views.PostRetrieveUpdateDestroyApiView.as_view()),

    path('ratings/', views.RatingListCreateApiView.as_view()),
    path('rating/<int:pk>/', views.RatingRetrieveUpdateDestroyAPIView.as_view()),

    path('comments/', views.CommentListCreateApiView.as_view()),
    path('comment/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
]

