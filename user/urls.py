from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from user import views
from user.custom_auth_token import obtain_auth_token

router = DefaultRouter()
router.register('login', views.LoginView, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.UserCreate.as_view(), name='signup'),
    re_path(r'^api-token-auth/', obtain_auth_token),
]
