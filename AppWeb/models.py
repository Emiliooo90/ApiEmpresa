from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

class Empleado(models.Model):
    rut_emp = models.CharField(primary_key=True, max_length=100)
    nom_emp = models.CharField(max_length=100)
    area_tra = models.CharField(max_length=100)
    cap_maq = models.BooleanField(False)
    cap_grua = models.BooleanField(False)
    cap_alt = models.BooleanField(False)
    qr_code = models.ImageField(blank=True, upload_to='qr_codes')

    def __str__(self):
        return self.nom_emp

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.nom_emp)
        qr_offset = Image.new('RGB', (310, 310), 'white')
        draw = ImageDraw.Draw(qr_offset)
        qr_offset.paste(qr_image)
        files_name = f'{self.rut_emp}-{self.nom_emp}qr.png'
        buffer = BytesIO()
        qr_offset.save(buffer, 'PNG')
        self.qr_code.save(files_name, File(buffer), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)
