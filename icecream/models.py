from django.db import models


# Create your models here.


class Mother(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Father(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100, null=True)

    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)

    father = models.ForeignKey(Father, on_delete=models.CASCADE)

    icecream = models.ForeignKey('IceCream', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name
class IceCream(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class IceCreamStore(models.Model):
    name = models.CharField(max_length=100, null=True)

    icecreams = models.ManyToManyField(IceCream)
    def __str__(self):
        return self.name





