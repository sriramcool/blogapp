# Generated by Django 3.0.7 on 2020-10-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0005_auto_20201014_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='tech_blog',
            name='q1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tech_blog',
            name='q2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tech_blog',
            name='q3',
            field=models.TextField(blank=True),
        ),
    ]
