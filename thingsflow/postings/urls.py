from django.urls import path

from postings.views import (
    PostingDetailView,
    PostingListView
)

urlpatterns = [
    path("/detail", PostingDetailView.as_view()),
    path("", PostingListView.as_view())
]
