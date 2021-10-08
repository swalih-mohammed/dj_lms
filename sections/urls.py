from django.urls import path

from .views import SectionListView, SectionDetailView

urlpatterns = [
    path('<pk>', SectionListView.as_view(), name='Section_list')
    # path('<pk>', SectionDetailView.as_view(), name='Section-detail'),
]
