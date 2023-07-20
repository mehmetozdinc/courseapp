# Generated by Django 4.2.2 on 2023-07-20 14:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_course_imageurl_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
