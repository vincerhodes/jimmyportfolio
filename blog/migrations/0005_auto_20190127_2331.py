# Generated by Django 2.1.2 on 2019-01-27 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190127_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_post',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_title',
        ),
    ]
