from django.urls import path

from postings.views import PostingDetailView

urlpatterns = [
    path("/detail", PostingDetailView.as_view()),
]
