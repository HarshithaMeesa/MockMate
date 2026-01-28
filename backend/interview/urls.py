from django.urls import path
from .views import ResumeUploadView, StartInterviewView

from .audio_upload import AudioUploadView

urlpatterns = [
path('upload-resume/', ResumeUploadView.as_view()),
    path('start-interview/', StartInterviewView.as_view()),]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
    path("upload-audio/", AudioUploadView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
