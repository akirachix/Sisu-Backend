# Generated by Django 5.0.7 on 2024-11-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kicd',
            fields=[
                ('kicd_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_id', models.IntegerField(default=1)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(default=1, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]
