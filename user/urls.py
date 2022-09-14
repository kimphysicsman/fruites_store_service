from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import UserView


# /user
urlpatterns = [
    path('', UserView.as_view()),
    path('/token', TokenObtainPairView.as_view(), name='token'),
    path('/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/<username>', UserView.as_view()),

]
