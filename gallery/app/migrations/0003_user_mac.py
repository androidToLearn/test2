<<<<<<< HEAD
# Generated by Django 5.2.1 on 2025-05-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_image_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mac',
            field=models.IntegerField(default=-1),
        ),
    ]
=======
# Generated by Django 5.2.1 on 2025-05-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_image_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mac',
            field=models.IntegerField(default=-1),
        ),
    ]
>>>>>>> 494cc95ff01940e6a9be0350084b1fd140572d7d
