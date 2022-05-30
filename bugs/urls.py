from django.urls import path
from .views import ReportBugView

urlpatterns = [
    path('report-bug/', ReportBugView.as_view(), name="report-bug"),
]
