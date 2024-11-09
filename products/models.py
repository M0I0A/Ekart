from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    brand=models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=200)
    price=models.FloatField()
    desc=models.TextField()
    image=models.ImageField(upload_to='media')
    image1=models.ImageField(upload_to='media',null=True)
    image2=models.ImageField(upload_to='media',null=True)
    image3=models.ImageField(upload_to='media',null=True)

    priority=models.IntegerField(default=0)
    deleteStatus=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title