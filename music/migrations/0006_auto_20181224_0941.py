# Generated by Django 2.1.4 on 2018-12-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20181224_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(blank=True, max_length=45, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='genere',
            name='name',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]