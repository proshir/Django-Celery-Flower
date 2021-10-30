from bulk_update_or_create.query import BulkUpdateOrCreateQuerySet
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=15)
    birthday=models.DateField(blank=True,null=True,default=timezone.now)
    def __str__(self):
        return self.first_name+" "+self.last_name
class Book(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    name=models.CharField(max_length=30)
    author=models.ForeignKey(Author,on_delete=CASCADE,related_name="books")
    genere_choices=[
        ('FI','Fiction'),
        ('NO','Novel'),
        ('PO','Poetry'),
        ('FA','Fantasy')
    ]
    genere=models.CharField(max_length=2,choices=genere_choices)
    date_writed=models.DateField(blank=True,null=True,default=timezone.now)
    score=models.IntegerField(verbose_name="score",default=0,blank=False)
    def __str__(self):
        return self.name
