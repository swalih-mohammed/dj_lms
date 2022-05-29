from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentListView, StudentDetailView, StudentCurrentCourseChangeView
from django.urls import path


# router = DefaultRouter()
# router.register(r'', UserViewSet, basename='users')
# urlpatterns = router.urls

urlpatterns = [

    # default
    path('',
         UserViewSet, name="users"),
    # default
    path('students/',
         StudentListView.as_view(), name="student-list"),
    # get user current course and level
    path('details/<int:pk>/',
         StudentDetailView.as_view(), name="details"),

    # get user current course and level pk is student id
    path('change-current-course/<pk>/',
         StudentCurrentCourseChangeView.as_view(), name="change-order"),
]
