# Generated by Django 4.2.7 on 2023-11-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_otherlinks_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
