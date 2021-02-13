from django.db import models

# Create your models here.
class Numbers(models.Model):
     num_1 = models.IntegerField()
     num_2 = models.IntegerField()
     plus = models.CharField(max_length=200)
     minus = models.CharField(max_length=200)
     result = models.IntegerField(null = True, blank = True)
     pic = models.FileField(upload_to="media", blank = True)
     
     class Meta:
          verbose_name_plural = 'Numbers'

     def __str__(self):
          #return 'numbers are {} and {}'.format(self.num_1, self.num_2)
          return f'Nums: {self.num_1}, {self.num_2}'