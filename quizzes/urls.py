from django.urls import path

from .views import QizDetailView

urlpatterns = [
    # path('', LessonListView.as_view(), name='Lesson_list'),
    path('<pk>', QizDetailView.as_view(), name='quiz_detail'),
    # path('lesson-completed-create/', LessonCompletedCreateView.as_view(),
    #      name='Lesson_complete_create'),
]
