# Relational database design:

# Section – holds categories/topics
# Post – belongs to a section, holds title + content
# Reply – belongs to a post, holds content
# related_name – lets you reference all of the instances of an object within that class:
#   Example:
#   section = Section.objects.get(name="Math")
#   all_posts = section.posts.all()  # grabs every post in that section


from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=100)

    # This __str__ method is not required, but when instances of the 
    def __str__(self):
        return self.name
    
class Post(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.section.name})"
    
class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to {self.post.title}"
