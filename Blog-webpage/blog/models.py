from django.db import models

# Create your models here.
class Blog(models.Model):
    name=models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        help_text="Enter the name"
    )
    content=models.TextField(
        help_text="Content of the blog")
    created_at= models.DateTimeField(
        auto_now_add=True, help_text="DATE AND TIME VLOG WAS CREATED"
    )
    author=models.CharField(
        max_length=100,
        help_text="Enter Author of the Blog"
    ) 
    description=models.TextField(
       null=True, blank=True,
       help_text=" Short desctiption of the blog")
    published= models.BooleanField(
        default=False, help_text=" Indicates whether the blog is published."
    )
    def __str__(self):
        return self.name