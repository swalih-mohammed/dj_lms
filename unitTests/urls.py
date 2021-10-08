from django.urls import path

from .views import UnitTestListView, unitTestDetailView, GradedUnitTestCreateView

urlpatterns = [
    path('<unitID>', UnitTestListView.as_view(), name='UnitTest_list'),
    path('<unitTestID>', unitTestDetailView.as_view(), name='UnitTest-detail'),
    path('create/', GradedUnitTestCreateView.as_view(),
         name='GradedUnitTest-create'),
]
