# Generated by Django 2.2.6 on 2020-02-15 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddiconnect', '0005_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]