from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Courses(models.Model):
    LEVELS = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Adavance', 'Adavance')
    ]

    MODES = [
        ('Online', 'Online'),
        ('Offline', 'Offline')
    ]
    image = models.ImageField(upload_to='cubes/')
    name = models.CharField(max_length=100, null=False)
    price = models.PositiveIntegerField(null=False)
    level = models.CharField(max_length=100, choices=LEVELS)
    duration = models.PositiveIntegerField()
    mode = models.CharField(max_length=50,choices=MODES)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

# One to many
class CourseReview(models.Model):
    RATINGS = [
        ('Worst', 'Worst'),
        ('Bad', 'Bad'),
        ('Good', 'Good'),
        ('Better', 'Better'),
        ('Best', 'Best')
    ]
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=50, choices=RATINGS)
    comment = models.TextField()
    data_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.course.name}"
    
# Mant to many
class Affiliates(models.Model):
    name = models.CharField(max_length=50, default='Affiliate')
    location = models.CharField(max_length=50, default='India')
    mode = models.CharField(max_length=50, choices=Courses.MODES)
    course = models.ManyToManyField(Courses, related_name='course')

    def __str__(self):
        return self.name

# One to one
class Certificate(models.Model):
    course = models.OneToOneField(Courses, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    issued_data = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Certificate for {self.course.name}"
