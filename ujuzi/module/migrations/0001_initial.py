# Generated by Django 5.0.7 on 2024-11-24 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facilitator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_id', models.AutoField(primary_key=True, serialize=False)),
                ('module_name', models.CharField(max_length=255)),
                ('total_marks', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('facilitator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facilitator.facilitator')),
            ],
        ),
    ]
