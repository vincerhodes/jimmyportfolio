# Generated by Django 2.1.2 on 2019-01-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20190124_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_URL',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]