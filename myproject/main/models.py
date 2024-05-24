from django.db import models
from filer.fields.image import FilerImageField

class Pictures(models.Model):
    name = models.CharField('Название', max_length=30)
    img = FilerImageField(null=True, blank=True, on_delete=models.DO_NOTHING)
    my_order = models.PositiveIntegerField("Порядок",
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Картинка"
        ordering = ['my_order']
        verbose_name_plural = "Картинки"
