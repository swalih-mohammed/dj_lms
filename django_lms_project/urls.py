
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),

    path('courses/', include('courses.urls')),
    path('sections/', include('sections.urls')),
    path('units/', include('units.urls')),
    path('lessons/', include('lessons.urls')),
    path('unitTests/', include('unitTests.urls')),
    path('unitFilms/', include('films.urls')),

]
