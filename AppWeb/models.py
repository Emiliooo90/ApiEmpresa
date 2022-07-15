from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

class Empleado(models.Model):
    rut = models.CharField(primary_key=True, max_length=100)
    nombre_completo = models.CharField(max_length=100)
    area_de_trabajo = models.CharField(max_length=100)
    curso_maquinaria = models.BooleanField(False)
    curso_grua = models.BooleanField(False)
    curso_altura = models.BooleanField(False)
    qr_code = models.ImageField(blank=True, upload_to='qr_codes')
    imagen_empleado = models.ImageField(blank=True)
    url_empleado = models.CharField(max_length=300, default="http://emiliosk11.pythonanywhere.com/empleado/rut/?format=json")

    def __str__(self):
        return self.nombre_completo

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.url_empleado)
        qr_offset = Image.new('RGB', (600, 600), 'white')
        draw = ImageDraw.Draw(qr_offset)
        qr_offset.paste(qr_image)
        files_name = f'{self.rut}-{self.nombre_completo}qr.pdf'
        buffer = BytesIO()
        qr_offset.save(buffer, 'PDF')
        self.qr_code.save(files_name, File(buffer), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)
