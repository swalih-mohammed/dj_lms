from django.urls import path

from .views import CourseListView, CourseEnrollView, CurrentCourseDetailView,  CourseDetailView, UnitDetailView, EnrolledCourseListView

urlpatterns = [
    path('<username>/<category>',
         CourseListView.as_view(), name='Course-list'),
    path('<username>/category/<category>/<order>/', CurrentCourseDetailView.as_view(),
         name='CourseEnrolled-list'),
    path('enroll/', CourseEnrollView.as_view(), name='Course-enroll'),
    path('<pk>/<username>', CourseDetailView.as_view(), name='Course-detail'),
    path('units/<unitId>/<username>',
         UnitDetailView.as_view(), name='Unit-detail'),

]
