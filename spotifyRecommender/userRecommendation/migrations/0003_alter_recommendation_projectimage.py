# Generated by Django 4.2.16 on 2024-11-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRecommendation', '0002_alter_recommendation_idrecommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='projectImage',
            field=models.ImageField(upload_to='userRecommendations/images/'),
        ),
    ]