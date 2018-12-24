from rest_framework import serializers

from . import models


class DiscsSerializer(serializers.ModelSerializer):
    subgeneres = serializers.StringRelatedField(many=True)
    artist = serializers.StringRelatedField()
    genere = serializers.StringRelatedField()

    class Meta:
        model = models.Disc
        fields = ("name", "year", "price", "qty", "genere", "artist", "subgeneres")


class GenereSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genere
        fields = ("name")


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = ("name")
