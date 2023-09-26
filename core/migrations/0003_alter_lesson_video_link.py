# Generated by Django 4.1.7 on 2023-08-12 09:54

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_enrollment_completed_lessons_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video_link',
            field=embed_video.fields.EmbedVideoField(default='https://youtu.be/Izl1IIzpn0g'),
            preserve_default=False,
        ),
    ]
