# Generated by Django 3.1.1 on 2021-02-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0005_remove_tag_post'),
        ('Post', '0009_post_posttag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='PostTag',
            field=models.ManyToManyField(blank=True, to='tag.Tag'),
        ),
    ]