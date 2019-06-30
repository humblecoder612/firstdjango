from django.db import models
from datetime import datetime
# Create your models here.




class Cat(models.Model):
    tut_cat=models.CharField(max_length=200)
    cat_sum=models.CharField(max_length=200)
    cat_link=models.CharField(max_length=200,default=1)

    class Meta:
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.tut_cat

class Series(models.Model):
    tut_ser=models.CharField(max_length=200)
    tut_cat=models.ForeignKey(Cat,default=1,verbose_name="Category", on_delete=models.SET_DEFAULT)
    ser_summary=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural="series"
    
    def __str__(self):
        return self.tut_ser

class Tut(models.Model):
    tut_title = models.CharField(max_length=200)
    tut_content = models.TextField()
    tut_publish = models.DateTimeField(
        'date published', default=datetime.now())
    tut_ser=models.ForeignKey(Series,default=1,verbose_name="Series",on_delete=models.SET_DEFAULT)
    tut_link=models.CharField(max_length=200,default=1)
    def __str__(self):
        return self.tut_title