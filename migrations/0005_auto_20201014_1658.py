# Generated by Django 3.0.7 on 2020-10-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0004_auto_20201014_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech_blog',
            name='image2',
            field=models.ImageField(blank=True, upload_to='tech/image2'),
        ),
        migrations.AlterField(
            model_name='tech_blog',
            name='image3',
            field=models.ImageField(blank=True, upload_to='tech/image3'),
        ),
    ]
