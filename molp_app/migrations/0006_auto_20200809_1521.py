# Generated by Django 3.0.7 on 2020-08-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molp_app', '0005_auto_20200801_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='xml',
            field=models.FileField(upload_to='problems/xmls/', verbose_name='input file'),
        ),
        migrations.AlterField(
            model_name='userproblem',
            name='xml',
            field=models.FileField(upload_to='problems/xmls/', verbose_name='input file'),
        ),
    ]
