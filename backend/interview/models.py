from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='resumes/')
    skills = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class InterviewSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
 
     #user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    eye_contact_score = models.FloatField(default=0)
    confidence_score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
