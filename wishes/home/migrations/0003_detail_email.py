# Generated by Django 4.0.6 on 2022-07-24 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_detail_delete_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='Email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]