from django.db import models
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=17)
    content = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY = (
        ('Teacher','Teacher'),
        ('Student','Student'),

    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=101)
    slug =  models.CharField(max_length=100, default=title)
    email = models.EmailField()
    salary = models.FloatField()
    details = models.TextField()
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices = CATEGORY)
    created_at = models.DateTimeField(default=now)

    
'''
    def __str__(self):
        return self.title  #-------- in admin panel it will show the no. sequence
    
    def __str__(self):
        return self.title  ------ in admin panel it will show the title

'''


