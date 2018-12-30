from django.views.generic import CreateView

from .models import Announcement


class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title', 'content', 'summary']
