from django.urls import path

from .views import AnnouncementCreateView

app_name = "announcement"
urlpatterns = [
    path("create/", AnnouncementCreateView.as_view(), name="announcement_create")
]
