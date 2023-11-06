from django.urls import path
from posts import views

urlpatterns = [
    path("", views.IssueListView.as_view(), name="list"),
    path("drafts/", views.DraftIssueListView.as_view(), name="drafts"),
    path("new/", views.IssueCreateView.as_view(), name="new"),
    path("<int:pk>/", views.IssueDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.IssueUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.IssuetDeleteView.as_view(), name="delete"),
    path("archived/", views.IssueArchivedView.as_view(), name="archived"),

]