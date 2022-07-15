# Generated by Django 4.0.4 on 2022-07-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0009_empleado_imagen_empleado_alter_empleado_url_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='curso_altura',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='curso_grua',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='curso_maquinaria',
        ),
        migrations.AddField(
            model_name='empleado',
            name='trabajo_en_altura',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empleado',
            name='trabajo_en_caliente',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empleado',
            name='trabajo_en_excavaciones',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empleado',
            name='trabajo_espacios_confinados',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empleado',
            name='trabajo_herramienta_electrica',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empleado',
            name='trabajo_señalero',
            field=models.BooleanField(default=False),
        ),
    ]
