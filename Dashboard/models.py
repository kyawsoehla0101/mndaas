from django.db import models
from ckeditor.fields import RichTextField
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from accounts.models import CustomUser


# chocices for post
POST_CATEGORY=(
    ("ST","Statment"),
    ("SP","Speech"),
    ("IN","Interview"),
    ("M","Military"),
    ("P","Party"),
    ("NA","NorthernAlliance"),
    ("FPNCC","FPNCC"),
)
# end post 


   




def unique_slugify(instance, slug):
        model = instance.__class__
        unique_slug = slug
        while model.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + get_random_string(length=4)
        return unique_slug
# post model
class Post(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=RichTextField(blank=True,null=True)
    category = models.CharField(
        max_length = 20,
        choices = POST_CATEGORY,
        default=''
        )
    image=models.ImageField(upload_to='post-images/',null=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    created=models.DateTimeField(auto_now=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)
    slug = models.SlugField(default="", null=False,blank=True,unique=True)
   
    class Meta:
        ordering=['-created']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self,slugify(self.title,allow_unicode=True))
        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
# end


    
