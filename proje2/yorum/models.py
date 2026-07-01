from django.db import models
# Create your models here.
class Yorum(models.Model):
    user=models.CharField(max_length=50)
    baslik=models.CharField( max_length=50)
    yorumu=models.TextField()
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now=True)
    slug=models.SlugField(null=False,default="")
    def __str__(self):
     return self.user + " | " + self.baslik