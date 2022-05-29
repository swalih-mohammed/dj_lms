from django.urls import path
from .views import CourseCategoryView, CourseListView, CourseEnrollView, CurrentCourseDetailView, UnitDetailView, EnrolledCourseListView

urlpatterns = [

    # course category
    path('course-categories/',
         CourseCategoryView.as_view(), name='course-categories'),

    # different levels of a course grouped under a category
    path('course-by-category-list/<user_id>/',
         CourseListView.as_view(), name='course-by-category-list'),

    # details of a course which is current
    path('course-current-detail/<user_id>/', CurrentCourseDetailView.as_view(),
         name='current-course-detail'),

    # details of unit in a course
    path('units/<unit_id>/<user_id>/', UnitDetailView.as_view(),
         name='unit-detail'),

    # enolled courses list for account page
    path('course-enrolled-list/<username>/<category>/',
         EnrolledCourseListView.as_view(), name='enrolled-courses-list'),

    # enrolling to a course
    path('enroll/', CourseEnrollView.as_view(), name='course-enroll'),
]
