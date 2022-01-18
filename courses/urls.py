from django.urls import path

from .views import CourseListView, CourseDetailView, SectionListView, SectionDetailView, UnitListView, UnitDetailView

urlpatterns = [
    path('', CourseListView.as_view(), name='Course-list'),
    path('<pk>/<username>', CourseDetailView.as_view(), name='Course-detail'),
    path('sections/<pk>', SectionDetailView.as_view(), name='Section-detail'),
    path('units/<unitId>/<username>',
         UnitDetailView.as_view(), name='Unit-detail'),

]
