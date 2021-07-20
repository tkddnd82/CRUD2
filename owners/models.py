from django.db import models


# Create your models here.

class Owner(models.Model):
    name  = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age   =  models.IntegerField()

    class Meta:
        db_table =  'owners' # 테이블 이름


class Dog(models.Model):
    name  = models.CharField(max_length=45)
    age   = models.IntegerField(default = 0)
    owner =  models.ForeignKey('Owner', on_delete=models.CASCADE) #owner_id

    class Meta:
        db_table =  'dogs'
