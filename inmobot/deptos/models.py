from django.db import models

# Create your models here.
class Inmueble(models.Model):
    STATUS = [
        ('NEW', 'New'),
        ('SEL', 'Selected'),
        ('DEL', 'Deleted'),
    ]
    location = models.CharField(max_length=200)
    price = models.BigIntegerField(null=False)
    area = models.IntegerField(null=False)
    mt_price = models.IntegerField(null=False)
    rooms = models.IntegerField(null=False)
    pub_date = models.CharField(max_length=100)
    ib = models.CharField(max_length=20,unique=True)
    url = models.URLField(null=False)
    status = models.CharField(max_length=3,
                            choices=STATUS,
                            default='NEW')

    def __str__(self):
        return self.location