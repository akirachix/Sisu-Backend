# Generated by Django 5.0.7 on 2024-11-25 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='question',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
