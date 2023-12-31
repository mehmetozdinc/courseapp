# Generated by Django 4.2.2 on 2023-07-03 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(db_index=True, default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='kurslar', to='courses.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]
