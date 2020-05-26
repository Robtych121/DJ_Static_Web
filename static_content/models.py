from django.db import models
from datetime import datetime

# Create your models here.
class Static_Page(models.Model):

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    
    name = models.CharField(max_length=254, default='')
    url = models.CharField(max_length=254, default='', unique=True)
    html = models.TextField(default='')
    css = models.TextField(default='')
    scripts = models.TextField(default='')
    YESNOCHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    published = models.CharField(max_length=3, default='No', choices=YESNOCHOICES)
    created_date = models.DateField(default=datetime.now)


    def __str__(self):
        return self.name