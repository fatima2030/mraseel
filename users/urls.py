from django.urls import path, include
from .views import RegistrationView,Login,PasswordResetView,ProfileDetailView,ProfileUpdateView,PasswordChangeView,check
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
app_name = 'users' 
urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register' ),
    path('login/', Login.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(next_page = "/user/logged_out/"), name='logout'),
    path('logged_out/', LogoutView.as_view(next_page=None,template_name="home.html"), name='logged_out'),
    path('reset_password/', PasswordResetView.as_view(), name='reset_password' ),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='user_profile' ),
    path('profile/me/', ProfileDetailView.as_view(is_me=True), name='me' ),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_update' ),
    path('change_password/', PasswordChangeView.as_view(success_url="/user/password_changed/"), name='password_change' ),
    path('password_changed/', PasswordChangeView.as_view(template_name="user/password_changed.html"), name='password_changed' ),
    path('home/', check.as_view(), name='check' ),



]
