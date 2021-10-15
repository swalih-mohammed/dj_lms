from django.urls import path

from .views import LessonDetailView, LessonCompletedCreateView, LessonListView

urlpatterns = [
    path('', LessonListView.as_view(), name='Lesson_list'),
    path('<pk>', LessonDetailView.as_view(), name='Lesson_detail'),
    path('lesson-completed-create/', LessonCompletedCreateView.as_view(),
         name='Lesson_complete_create'),
]
