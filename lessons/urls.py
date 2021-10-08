from django.urls import path

from .views import LessonDetailView, LessonTestView, LessonCompletedCreateView, LessonListView

urlpatterns = [
    path('', LessonListView.as_view(), name='Lesson_list'),
    path('<pk>', LessonDetailView.as_view(), name='Lesson_detail'),
    path('<pk>/tests', LessonTestView.as_view(), name='Lesson_tests'),
    path('lesson-completed-create/', LessonCompletedCreateView.as_view(),
         name='Lesson_complete_create'),
]
