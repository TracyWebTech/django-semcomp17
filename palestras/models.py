from django.db import models


class Palestra(models.Model):
    # titulo
    titulo = models.CharField(max_length=20)

    # palestrante
    palestrante = models.CharField(max_length=20)

    # horario
    horario = models.DateTimeField()

    def __unicode__(self):
        return u'{} ({})'.format(self.titulo, 
                                 self.palestrante)

