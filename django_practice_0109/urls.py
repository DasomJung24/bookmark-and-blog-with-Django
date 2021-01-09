from django.contrib import admin
from django.urls import path

from bookmark.views import BookmarkListView, BookmarkDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', BookmarkListView.as_view(), name='index'),
    path('bookmark/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
]
