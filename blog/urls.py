from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('track_user/',views.track_user,name = 'track_user'),
    path('stop-tracking/',views.stop_tracking,name = 'stop-tracking'),
    path('cookie/', views.test_cookie,name='cookie'),
    path('',views.post_list, name='post_list'),
    path('<pk>/', views.post_detail, name='post_detail'),
 #   path('<pk>/', views.post_detail, name='post_detail'),
    path('category/<category_slug>/', views.post_by_category, name='post_by_category'),
    path('tag/<tag_slug>/', views.post_by_tag, name='post_by_tag'),
    path('blog/', views.test_redirect, name = 'test_redirect'),
    path('feedback/', views.feedback,name = 'feedback'),
]