from django.urls import path

from .views import ConversationDetailView,  ConversationCompletedCreateView

urlpatterns = [

    path('<pk>', ConversationDetailView.as_view(), name='conversation_detail'),
    path('conversation-completed-create/', ConversationCompletedCreateView.as_view(),
         name='Conversation_complete_create'),

]
