# Generated by Django 5.0.1 on 2024-01-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktitle', models.TextField(max_length=40)),
                ('taskdesc', models.CharField(max_length=500)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
