# Generated by Django 2.1.4 on 2018-12-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20181224_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgenre',
            name='disc',
        ),
        migrations.RemoveField(
            model_name='subgenre',
            name='genere',
        ),
        migrations.AddField(
            model_name='disc',
            name='subgenere',
            field=models.ManyToManyField(blank=True, related_name='subgeneres', to='music.Genere'),
        ),
        migrations.DeleteModel(
            name='Subgenre',
        ),
    ]