# Generated by Django 2.1.4 on 2018-12-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20181224_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]