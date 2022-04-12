from django.urls import path

from .views import CourseListView, CourseEnrollView, CourseDetailView, SectionListView, SectionDetailView, UnitListView, UnitDetailView, EnrolledCourseListView

urlpatterns = [
    path('<category>', CourseListView.as_view(), name='Course-list'),
    path('<username>/<category>', EnrolledCourseListView.as_view(),
         name='CourseEnrolled-list'),
    path('enroll/', CourseEnrollView.as_view(), name='Course-enroll'),
    path('<pk>/<username>', CourseDetailView.as_view(), name='Course-detail'),
    path('sections/<pk>', SectionDetailView.as_view(), name='Section-detail'),
    path('units/<unitId>/<username>',
         UnitDetailView.as_view(), name='Unit-detail'),

]
