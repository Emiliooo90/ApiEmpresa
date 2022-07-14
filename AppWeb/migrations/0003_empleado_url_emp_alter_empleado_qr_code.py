# Generated by Django 4.0.4 on 2022-07-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0002_empleado_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='url_emp',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]