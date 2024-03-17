from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    follows = models.ManyToManyField("Profile", related_name="followed_by", symmetrical=False, blank=True)
    bio = models.TextField(blank=True, null=True, max_length=500)
    profile_picture = models.ImageField(upload_to="profile_images", default="blank-profile-picture.png")
    date_of_birth = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.username
