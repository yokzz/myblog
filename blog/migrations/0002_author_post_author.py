# Generated by Django 5.0.3 on 2024-03-17 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.author'),
        ),
    ]