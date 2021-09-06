# Generated by Django 3.2.6 on 2021-09-06 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_alter_photo_file'),
        ('users', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='rooms.room'),
        ),
    ]
