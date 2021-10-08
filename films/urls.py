from django.urls import path

from .views import UnitFilmListView, unitFilmDetailView

urlpatterns = [
    path('<unitID>', UnitFilmListView.as_view(), name='UnitFilm_list'),
    path('<unitFilmID>', unitFilmDetailView.as_view(), name='UnitFilm-detail'), ]
