# Generated by Django 4.2.16 on 2024-11-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idRecommendation', models.CharField(max_length=12)),
                ('projectName', models.CharField(max_length=50)),
                ('spotifyUrl', models.URLField()),
                ('projectImage', models.ImageField(upload_to='spotifyRecommender/images/')),
                ('artistName', models.CharField(max_length=30)),
            ],
        ),
    ]
