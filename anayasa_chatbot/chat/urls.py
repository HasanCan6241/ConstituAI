# chat/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import register_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chat/', views.chat, name='chat'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('history/', views.history, name='history'),
    path('conversation/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),

    # Kullanıcı yetkilendirme
    path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register_view, name='register'),
]