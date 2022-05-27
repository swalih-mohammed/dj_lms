from django.urls import path
from .views import CourseListView, CourseEnrollView, CurrentCourseDetailView, UnitDetailView, EnrolledCourseListView

urlpatterns = [

    # different levels of a course grouped under a category
    path('course-by-category-list/<username>/<category>/',
         CourseListView.as_view(), name='course-by-category-list'),

    # details of a course which is current
    path('course-current-detail/<username>/<category>/<order>/', CurrentCourseDetailView.as_view(),
         name='current-course-detail'),

    # enolled courses list for account page
    path('course-enrolled-list/<username>/<category>/',
         EnrolledCourseListView.as_view(), name='enrolled-courses-list'),

    # enrolling to a course
    path('enroll/', CourseEnrollView.as_view(), name='course-enroll'),
]
