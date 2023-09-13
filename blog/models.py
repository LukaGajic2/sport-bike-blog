"""
Database models for the blog app
& comments section.
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

BIKE_CATEGORY = (
    ('standards', 'Standard'),
    ('sport', 'Sport'),
    ('sport-touring', 'Sport Touring'),
    ('touring', 'Touring'),
    ('cruiser', 'Cruiser'),
    ('off-road', 'Off Road'),
)


# Model made by help from "I think therefore I blog" walkthrough

class BlogPost(models.Model):
    """
    Database model for submitting a blog post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    engine_cc = models.IntegerField(default=0, null=False, blank=False)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(
        max_length=50, choices=BIKE_CATEGORY, null=False, blank=False,
        default='standards')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        Displays blog posts in descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        Returns total number of post likes
        """
        return self.likes.count()


# Model used from "I think therefore I blog" walkthrough.

class BlogComment(models.Model):

    """
    Database model for creating a comment
    on a blog post
    """
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order comments in ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Display the comment as the comment text,
        and comment author name
        """
        return f"Comment {self.body} by {self.name}"
