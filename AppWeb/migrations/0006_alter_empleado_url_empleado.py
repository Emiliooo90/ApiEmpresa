# Generated by Django 4.0.4 on 2022-07-14 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0005_rename_area_tra_empleado_area_de_trabajo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='url_empleado',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
