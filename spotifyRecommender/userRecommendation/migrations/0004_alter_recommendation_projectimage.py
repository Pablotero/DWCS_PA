# Generated by Django 4.2.16 on 2024-11-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRecommendation', '0003_alter_recommendation_projectimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='projectImage',
            field=models.ImageField(upload_to='userRecommendation/images/'),
        ),
    ]
