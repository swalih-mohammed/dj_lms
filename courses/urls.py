from django.urls import path

from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('', CourseListView.as_view(), name='Course_list'),
    path('<pk>', CourseDetailView.as_view(), name='Course-detail'), ]
