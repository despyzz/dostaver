# Generated by Django 4.2.7 on 2023-11-20 20:15

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_importantinformation_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacyblocks',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True),
        ),
    ]
