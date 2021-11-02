from django.urls import path, include
from accounts import views as accounts_views

app_name = "accounts"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("create/", accounts_views.RegisterView.as_view(), name="register"),
    path("<int:pk>", accounts_views.UserDetailView.as_view(), name="profile"),
    path('<int:pk>/change/', accounts_views.UserChangeView.as_view(), name='change'),
    path("<int:pk>/change-password/", accounts_views.UserPasswordChangeView.as_view(), name="change_password")
]