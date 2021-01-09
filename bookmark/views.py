from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkDetailView(DetailView):
    model = Bookmark
