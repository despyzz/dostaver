# Generated by Django 4.2.7 on 2023-11-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_privacyblocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessesBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField(blank=True)),
                ('align', models.TextField()),
            ],
        ),
    ]
