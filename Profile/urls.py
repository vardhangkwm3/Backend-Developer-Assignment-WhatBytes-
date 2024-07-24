from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.LOGIN, name="login"),
    path('signup/',views.Signup, name="signup"),
    path('home/',views.Home, name="home"),
    path('logout/',views.LogOut, name="logout"),
    path('profile/',views.Profile, name="profile"),
    path('change/',views.ChangePassword, name="change"),
    path('pass_reset/',auth_views.PasswordResetView.as_view(template_name = 'PassReset/ResetForm.html'), name='pass_reset'),
    path('pass_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name = 'PassReset/ResetDone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'PassReset/ResetConfirm.html'), name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name = 'PassReset/ResetComplete.html'), name='password_reset_complete'),
]