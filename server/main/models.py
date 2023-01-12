from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=25)

##? favourites_set attribute is the one-to-many link to Favourites model and is array of

  def __str__(self):
    return self.name


class Favourites(models.Model):
  favslist = models.ForeignKey(User, on_delete=models.CASCADE)
  ticker = models.CharField(max_length=8)
  isfav = models.BooleanField()

  def __str__(self):
    return self.ticker