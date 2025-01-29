from django.db import models
from django.urls import reverse
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/')  # this path is where the video files will be stored
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Represents gym membership plans
class MembershipPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

# Represents gym trainers
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    specialties = models.CharField(max_length=200, default="Generalist")  # Provide a default value

    def __str__(self):
        return self.name


# Represents gym class categories
class ClassCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
# Model for Gym Schedule
class Schedule(models.Model):
    user_name = models.CharField(max_length=100)
    membership = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    class_category = models.ForeignKey(ClassCategory, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    session_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user_name} - {self.class_category} with {self.trainer} at {self.session_time}"