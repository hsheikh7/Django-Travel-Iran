# Generated by Django 4.1.7 on 2023-04-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='blog/'),
            preserve_default=False,
        ),
    ]
