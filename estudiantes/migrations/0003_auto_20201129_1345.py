# Generated by Django 2.2.14 on 2020-11-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_auto_20201129_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
