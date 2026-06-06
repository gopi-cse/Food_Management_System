from django.urls import path

from .views import ProfileView, RegisterView, UserLoginView, UserLogoutView, UserPasswordChangeView

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("change-password/", UserPasswordChangeView.as_view(), name="change_password"),
]
