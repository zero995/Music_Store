# Generated by Django 2.1.4 on 2018-12-24 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apikey',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=70),
        ),
    ]