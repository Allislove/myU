# Generated by Django 2.2.14 on 2020-12-01 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0003_auto_20201130_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='estudiante',
            field=models.ManyToManyField(related_name='Clase', to='estudiantes.Estudiante'),
        ),
    ]
