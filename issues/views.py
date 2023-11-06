
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Issues, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.core.exceptions import PermissionDenied


class IssueListView(ListView):
    template_name ="issues/list.html"
    model = Issues
    fields = ["summary", "description", "assignee", "status"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (
            context["issue"].status.name == "draft" and 
            cntext["issue"].author != self.request.user
            ):
            raise PermissionDenied()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_status = Status.objects.get(name="published")
        context["issue_list"] = Post.objects.filter(
            status=published_status
            ).order_by('created_on').reverse()
        return context

class DraftPostListView(ListView):
    template_name = "issues/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="draft")
        context["issue_list"] = Post.objects.filter(
            status=draft_status
        ).filter(
            author=self.request.user
        ).order_by("created_on").reverse()
        return context

class PostArchivedView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archived_status = Status.objects.get(name="archived")
        context["issue_list"] = Issue.objects.filter(
            status=archived_status
        ).filter(
            author=self.request.user
        ).order_by("created_on").reverse()
        return context
