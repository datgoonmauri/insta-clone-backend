# Generated by Django 3.0.8 on 2020-07-13 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_uploads/')),
                ('caption', models.TextField(max_length=500)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='authors_who_like_this', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
