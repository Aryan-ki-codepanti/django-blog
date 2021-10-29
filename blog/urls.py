from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name="BlogHome"),
    path('<str:slug>/', views.blogPost, name="BlogPost"),
    path('post-comment/<int:post_sno>' , views.postComment , name="PostComment" ),
    path('<int:post_sno>/post-reply/<int:comment_sno>/' , views.postReply , name="PostReply" )
]
