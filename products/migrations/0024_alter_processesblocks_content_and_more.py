# Generated by Django 4.2.7 on 2023-11-20 20:18

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_privacyblocks_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processesblocks',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True),
        ),
        migrations.AlterField(
            model_name='processesblocks',
            name='title',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
