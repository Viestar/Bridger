# Generated by Django 3.2.9 on 2022-01-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
