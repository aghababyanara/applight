# Generated by Django 4.2 on 2025-01-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applight', '0002_alter_about_options_alter_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='icon',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]