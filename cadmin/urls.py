from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('register/',views.register,name = 'register'),
    path('password-change-done/',auth_views.PasswordChangeDoneView.as_view(template_name = 'cadmin/password_change_done.html'),name='password_change_done'),
    path('password-change/',auth_views.PasswordChangeView.as_view(template_name = 'cadmin/password_change.html' ,),name = 'password_change'),
    path('login/', auth_views.LoginView.as_view(template_name='cadmin/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'cadmin/logout.html'),name = 'logout'),
    path('post/add/', views.post_add, name ='post_add'),
    path('post/update/<pk>/',views.post_update, name='post_update'),
]