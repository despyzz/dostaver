# Generated by Django 4.2.7 on 2023-11-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_privacyblocks_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='processesblocks',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]