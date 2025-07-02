from django.urls import path, include
from .views import UserSignupView, UserLoginView, UserLogoutView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    # ✅ This includes both base and token auth URLs
    path('auth/', include([
        path('', include('djoser.urls')),
        path('', include('djoser.urls.authtoken')),
    ])),
]
