from django.urls import path, include
from .views import RegisterView, LoginView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('user/', UserView.as_view(), name='user_detail'),
]
