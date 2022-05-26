
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from allauth.account.views import ConfirmEmailView


# from rest_auth.views import (
#     LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
#     PasswordResetView, UserDetailsView,
# )

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('lessons/', include('lessons.urls')),
    path('quizzes/', include('quizzes.urls')),
    path('conversations/', include('conversations.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),


]
