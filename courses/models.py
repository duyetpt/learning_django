from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    educator = models.CharField(max_length=50)
    description = models.TextField(default="")
    excerpt = models.TextField(max_length=300, default="")
    num_lessons = models.PositiveSmallIntegerField(default=0)
    picture = models.ImageField(upload_to="course_pictures")

    def __str__(self):
      return self.name
