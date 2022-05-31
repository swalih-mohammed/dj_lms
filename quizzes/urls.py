from django.urls import path

from .views import GeneralQuizListView, QizDetailView, QuizCompletedCreateView

urlpatterns = [
    path('category/<category>/<username>',
         GeneralQuizListView.as_view(), name='Lesson_list'),
    path('<pk>/<user_id>', QizDetailView.as_view(), name='quiz_detail'),
    path('quiz-completed-create/', QuizCompletedCreateView.as_view(),
         name='Quiz_complete_create'),
    # path('lesson-completed-create/', LessonCompletedCreateView.as_view(),
    #      name='Lesson_complete_create'),
]
