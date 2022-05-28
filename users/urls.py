from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentDetailView
from django.urls import path


# router = DefaultRouter()
# router.register(r'', UserViewSet, basename='users')
# urlpatterns = router.urls

urlpatterns = [

    # default
    path('',
         UserViewSet, name="users"),
    path('details/<int:pk>/',
         StudentDetailView.as_view(), name="details"),
]
