# Generated by Django 4.2.16 on 2024-11-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendationId', models.CharField(blank=True, max_length=12)),
                ('profileName', models.CharField(help_text='Introduce your profileName', max_length=30)),
                ('profilePhoto', models.ImageField(upload_to='spotifyRecommender/images/')),
                ('urlSpotify', models.URLField(help_text='Introduce your spotify profile URL')),
            ],
        ),
    ]