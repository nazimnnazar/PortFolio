from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('posts',views.posts,name='posts'),   
    path('post/<slug:slug>',views.post,name='post'),
    path('profile',views.profile,name='profile'),
    #Posts Editing
	path('create_post/', views.createPost, name="create_post"),
	path('update_Post/<slug:slug>/', views.updatePost, name="update_Post"),
    path('delete_Post/<slug:slug>/',views.deletePost,name='delete_Post'),
    #Email
    path('send_Email',views.sendEmail,name='send_Email'),
    #404
    path('error',views.error,name='error'),
]