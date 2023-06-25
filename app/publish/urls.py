from django.urls import path
from publish import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up', views.sign_up, name='sign-up'),
    path('login', views.login_view, name='login'), 
    path('logout', views.logout_view, name='logout'), 
]
