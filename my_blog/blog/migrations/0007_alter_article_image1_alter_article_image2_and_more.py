# Generated by Django 4.1.2 on 2022-11-28 19:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_sectionlabel2_article_sectionlabel3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='image2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='image3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]