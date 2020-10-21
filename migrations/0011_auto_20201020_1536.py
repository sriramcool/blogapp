# Generated by Django 3.0.7 on 2020-10-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0010_auto_20201020_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='picture',
            new_name='post',
        ),
        migrations.AddField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'like'), ('unlike', 'unlike')], default='Like', max_length=10),
        ),
    ]