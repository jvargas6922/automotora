from django.urls import path, include
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('list_card/', views.list_card, name='list_card'),

]
