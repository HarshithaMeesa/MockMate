from django.urls import path
from .views import ResumeUploadView, StartInterviewView


urlpatterns = [
path('upload-resume/', ResumeUploadView.as_view()),
    path('start-interview/', StartInterviewView.as_view()),]
