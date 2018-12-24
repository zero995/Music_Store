# Create your tests here.

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from music import models
from music import serializers


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    def create_artist(self):
        self.a1 = models.Artist.objects.create(name="Fall Out Boy")
        self.a2 = models.Artist.objects.create(name="Michael Jackson")
        self.a3 = models.Artist.objects.create(name="Mecano")

    def create_genere(self):
        self.g1 = models.Genere.objects.create(name="Pop")
        self.g2 = models.Genere.objects.create(name="Rock")

    def create_album(sefl, name, year, genere, qty, price, artist):
        models.Disc.objects.create(name=name, year=year, genere=genere, qty=qty, price=price, artist=artist)

    def setUp(self):
        # add test data
        self.create_artist()
        self.create_genere()
        self.create_album("infinity on high", "2000", self.g2, 50, 170, self.a1)
        self.create_album("Thriller", "2000", self.g1, 150, 300, self.a2)
        self.create_album("Mecano", "2000", self.g1, 70, 150, self.a3)


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("list-all")
        )
        # fetch the data from db
        expected = models.Disc.objects.all()
        serialized = serializers.DiscsSerializer(expected, many=True)
        self.assertEqual(response.json(), serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
