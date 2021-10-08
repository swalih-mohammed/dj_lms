from django.urls import path

from .views import UnitDetailView

urlpatterns = [
    # path('<pk>', UnitListView.as_view(), name='unit_list')
    path('<unitId>/<username>', UnitDetailView.as_view(), name='unit-detail'),
]
