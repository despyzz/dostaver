# Generated by Django 4.2.7 on 2023-11-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callbacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbackrequests',
            name='callback_type',
            field=models.TextField(default='hello123'),
            preserve_default=False,
        ),
    ]
