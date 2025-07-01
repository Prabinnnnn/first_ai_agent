from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
User = settings.AUTH_USER_MODEL #this points to the custom user model Django uses
class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #this creates many to one relationship, may documents to one user, and foreign key links each document to a specific user
    title = models.CharField(max_length=50, default="Title")
    content = models.CharField(blank=True, null=True)
    active = models.BooleanField(default=True)
    active_at = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    created_at =models.DateTimeField(auto_now_add=True) #this will auto generate the timestamos when the document is created, it only sets the value once at creation
    updated_at = models.DateTimeField(auto_now=True) #auto update the timestamp everytime the model is saved

    def __str__(self):
        return f"<Document: {self.title}"

    def save(self, *args, **kwargs):
        if self.active and self.active_at is None:
            self.active_at = timezone.now()
        else:
            self.active_at = None
        super().save(*args, **kwargs)
