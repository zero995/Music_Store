from django.db import models


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.PositiveIntegerField(blank=True, null=True)
    comment = models.TextField()
    disc = models.ForeignKey('Disc', models.DO_NOTHING)


class Disc(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    year = models.IntegerField()
    price = models.IntegerField()
    qty = models.IntegerField()
    artist = models.ForeignKey(Artist, models.DO_NOTHING)
    genere = models.ForeignKey('Genere', models.DO_NOTHING)
    subgeneres = models.ManyToManyField('Genere', related_name="subgeneres", blank=True)
    def __str__(self):
        return self.name


class Genere(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    unit_price = models.PositiveIntegerField()
    qty = models.PositiveIntegerField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    disc = models.ForeignKey(Disc, models.DO_NOTHING)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    apikey = models.CharField(max_length=45, blank=True)
    email = models.EmailField(max_length=70, unique=True)


class UserHasComment(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    comment = models.ForeignKey(Comment, models.DO_NOTHING)
