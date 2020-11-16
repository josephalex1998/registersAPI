from django.db import models

# Create your models here.

class Registers(models.Model):
    name = models.CharField(max_length = 50, blank = False, default = '')
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length = 50, blank = False, default = '')
    password = models.CharField(max_length = 50, blank = False, default = '')
    confirmPassword = models.CharField(max_length = 50, blank = False, default = '')

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('id',)