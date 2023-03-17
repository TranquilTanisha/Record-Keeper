from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, null=True, blank=True)
    email=models.EmailField(max_length=500, null=True, blank=True)
    short_intro= models.TextField(max_length=500, null=True, blank=True)
    username=models.CharField(max_length=200, null=True, blank=True)
    profile_image=models.ImageField(upload_to="images/profile/", default="profiles/user-default.png", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)
    
# class Suggestion(models.Model):
#     sender=models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
#     recipient=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
#     #name=models.CharField(max_length=200, null=True, blank=True)
#     #email=models.EmailField(max_length=500, null=True, blank=True)
#     subject=models.TextField(max_length=1000, null=True, blank=True)
#     is_read=models.BooleanField(default=False)
#     created=models.DateTimeField(auto_now_add=True)
#     id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.name)
    
#     class Meta:
#         ordering=["is_read", "-created"]