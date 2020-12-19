from workers import views
from workers.views import Login,RegistrationView,ProfileDetailView,JobsView
from django.urls import path


app_name = 'workers'


urlpatterns = [
  
    path('register/', RegistrationView.as_view(), name='worker_user' ),
    path('login2/', Login.as_view(), name='login2' ),
    path('profile/me/', ProfileDetailView.as_view(is_me=True), name='me' ),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='user_profile' ),
    path('Jobs/', JobsView.as_view(), name='Jobs' ),






]


