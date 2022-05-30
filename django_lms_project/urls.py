
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from allauth.account.views import ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('lessons/', include('lessons.urls')),
    path('quizzes/', include('quizzes.urls')),
    path('conversations/', include('conversations.urls')),
    path('bugs/', include('bugs.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
    path('dj-rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),


]
