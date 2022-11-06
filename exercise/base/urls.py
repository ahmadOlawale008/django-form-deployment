from django.urls import path
from django.contrib import admin
from . import views
app_name = 'basic_app'

urlpatterns= [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout_tag'),
    path('special/', views.special, name='special')
]