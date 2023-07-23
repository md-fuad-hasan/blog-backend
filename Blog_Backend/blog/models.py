from django.db import models
from account.models import Account
import uuid 

from django.db.models.signals import pre_save,post_delete
from django.utils.text import slugify
from django.dispatch import receiver 

# Create your models here.

def blog_image_uploaded(instance,filename):
    return 'blog_images/{username}/{filename}'.format(username=instance.author.username,filename=filename)

class Blog(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=255)
    blog_content = models.TextField()
    blog_image = models.ImageField(upload_to=blog_image_uploaded)
    slug = models.SlugField(max_length=255,blank=True,unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ["-publish_date"]

    def __str__(self):
        return self.blog_title


@receiver(post_delete, sender=Blog)
def pre_save_receiver(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.blog_title)+"-"+str(uuid.uuid4())
pre_save.connect(pre_save_receiver, sender=Blog)