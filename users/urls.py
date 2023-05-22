from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', views.UserCreate.as_view()),
    path('detail/', views.UserDetail.as_view()),
    path('update/', views.UserUpdate.as_view()),
    path('search/', views.UserSearch.as_view()),
    path('delete/', views.UserDelete.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.UserLogout.as_view()),
    path('password/find/', views.UserPasswordFind.as_view()),
    path('password/change/', views.UserPasswordChange.as_view()),
]
