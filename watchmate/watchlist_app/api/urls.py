from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path("list/", views.WatchListAV.as_view(), name="watch-list"),
    path("<int:pk>/", views.WatchDetailAV.as_view(), name="watch-detail"),
    path("stream/list/", views.StreamPlatformListAV.as_view(), name="stream-list"),
    path("stream/<int:pk>/", views.StreamPlatformDetailAV.as_view(), name="stream-detail"),
]
