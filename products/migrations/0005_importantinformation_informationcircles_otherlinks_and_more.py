# Generated by Django 4.2.7 on 2023-11-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_callbackrequests'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'ImportantInformation',
            },
        ),
        migrations.CreateModel(
            name='InformationCircles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'InformationCircles',
            },
        ),
        migrations.CreateModel(
            name='OtherLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'OtherLinks',
            },
        ),
        migrations.CreateModel(
            name='ProcessesCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'ProcessesCards',
            },
        ),
        migrations.CreateModel(
            name='RatesTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
