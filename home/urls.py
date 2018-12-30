from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


app_name = 'home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html'), name='index'),
    path('announcements/', include('announcement.urls', namespace='announcements')),
    # ^^ This is temporary
    path('admin/', admin.site.urls)
]
