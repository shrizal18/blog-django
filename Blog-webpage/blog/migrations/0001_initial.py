# Generated by Django 5.1.4 on 2024-12-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name', max_length=200, unique=True)),
                ('content', models.TextField(help_text='Content of the blog')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='DATE AND TIME VLOG WAS CREATED')),
                ('author', models.CharField(help_text='Enter Author of the Blog', max_length=100)),
                ('published', models.BooleanField(default=False, help_text=' Indicates whether the blog is published.')),
            ],
        ),
    ]
