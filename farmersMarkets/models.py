from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=100)

class State(models.Model):
    state_full = models.CharField(max_length=100)
    state_abbr = models.CharField(max_length=2)

class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=100)

class City(models.Model):
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Market(models.Model):
    market_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zip = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()

class MarketsCategories(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    date_time = models.DateField()
    score = models.IntegerField()
    review = models.TextField()
