# Generated by Django 4.2 on 2025-01-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applight', '0004_alter_video_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='icon',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
