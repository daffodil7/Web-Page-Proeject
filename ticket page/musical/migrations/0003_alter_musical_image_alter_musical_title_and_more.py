# Generated by Django 4.0.7 on 2022-09-27 11:21

from django.db import migrations, models
import photo.fields


class Migration(migrations.Migration):

    dependencies = [
        ('musical', '0002_alter_musical_options_remove_musical_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musical',
            name='image',
            field=photo.fields.ThumbnailImageField(upload_to='photo/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='musical',
            name='title',
            field=models.CharField(max_length=30, verbose_name='TITLE'),
        ),
        migrations.AlterField(
            model_name='musical',
            name='upload_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Upload Date'),
        ),
    ]
