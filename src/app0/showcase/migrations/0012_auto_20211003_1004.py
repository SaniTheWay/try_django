# Generated by Django 3.2.7 on 2021-10-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0011_alter_showcase_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showcase',
            name='price',
        ),
        migrations.RemoveField(
            model_name='showcase',
            name='summary',
        ),
        migrations.AddField(
            model_name='showcase',
            name='project_img',
            field=models.ImageField(default=True, upload_to='img/'),
            preserve_default=False,
        ),
    ]
