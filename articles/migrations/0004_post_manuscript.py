# Generated by Django 3.1.7 on 2021-04-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210327_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='manuscript',
            field=models.FileField(blank=True, upload_to='manuscripts/'),
        ),
    ]
