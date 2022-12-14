# Generated by Django 4.0.7 on 2022-09-27 11:20

from django.db import migrations, models
import photo.fields


class Migration(migrations.Migration):

    dependencies = [
        ('musical', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musical',
            options={'ordering': ('title',)},
        ),
        migrations.RemoveField(
            model_name='musical',
            name='name',
        ),
        migrations.AddField(
            model_name='musical',
            name='image',
            field=photo.fields.ThumbnailImageField(blank=True, null=True, upload_to='photo/%Y/%m'),
        ),
        migrations.AddField(
            model_name='musical',
            name='title',
            field=models.CharField(default='제목', max_length=30, verbose_name='TITLE'),
        ),
        migrations.AddField(
            model_name='musical',
            name='upload_dt',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Upload Date'),
        ),
        migrations.DeleteModel(
            name='Poster',
        ),
    ]
