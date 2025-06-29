from django.urls import path, include
from .views import UserSignupView, UserLoginView, UserLogoutView
 
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('auth/', include('djoser.urls')), # includes /auth/password/reset/
    path('auth/', include('djoser.urls.authtoken')),  # includes login/logout with token
]