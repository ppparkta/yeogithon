from django.db import models

# Create your models here.
class Post(models.Model):
    swuniName = models.ForeignKey('user.Swuni', on_delete=models.CASCADE, related_name="swuniName" )
    title = models.CharField(max_length=100)
    regTime = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    like = models.ManyToManyField('user.Swuni', related_name="swuniLike")