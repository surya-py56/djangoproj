# Generated by Django 4.1.6 on 2023-06-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_deleted',
            field=models.CharField(default='N', max_length=5),
            preserve_default=False,
        ),
    ]