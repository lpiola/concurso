from django.db import models
from datetime import date


# Create your models here.
ESTADOS_VISTA_LIMPIDEZ =[
        (5, 'excelente'),
        (4, 'muybueno'),
        (3, 'bueno'),
        (2, 'regular'),
        (1, 'insuficiente'),    
    ]
ESTADOS_VISTA_COLOR =[
        (10, 'excelente'),
        (8, 'muybueno'),
        (6, 'bueno'),
        (4, 'regular'),
        (2, 'insuficiente'),    
    ]
ESTADOS_OLFATO_INTENSIDAD =[
        (8, 'excelente'),
        (7, 'muybueno'),
        (6, 'bueno'),
        (4, 'regular'),
        (2, 'insuficiente'),    
    ]
ESTADOS_OLFATO_FRANQUEZA =[
        (6, 'excelente'),
        (5, 'muybueno'),
        (4, 'bueno'),
        (3, 'regular'),
        (2, 'insuficiente'),    
    ]
ESTADOS_OLFATO_CALIDAD =[
        (16, 'excelente'),
        (14, 'muybueno'),
        (12, 'bueno'),
        (10, 'regular'),
        (8, 'insuficiente'),    
    ]
ESTADOS_GUSTO_INTENSIDAD =[
        (8, 'excelente'),
        (7, 'muybueno'),
        (6, 'bueno'),
        (4, 'regular'),
        (2, 'insuficiente'),    
    ]
ESTADOS_GUSTO_FRANQUEZA =[
        (6, 'excelente'),
        (5, 'muybueno'),
        (4, 'bueno'),
        (3, 'regular'),
        (2, 'insuficiente'),    
    ]
ESTADOS_GUSTO_CALIDAD =[
        (22, 'excelente'),
        (19, 'muybueno'),
        (16, 'bueno'),
        (13, 'regular'),
        (10, 'insuficiente'),    
    ]
ESTADOS_GUSTO_PERSISTENCIA =[
        (8, 'excelente'),
        (7, 'muybueno'),
        (6, 'bueno'),
        (5, 'regular'),
        (4, 'insuficiente'),    
    ]
ESTADOS_APRECIACION_GLOBAL =[
        (11, 'excelente'),
        (10, 'muybueno'),
        (9, 'bueno'),
        (8, 'regular'),
        (7, 'insuficiente'),    
    ]
class Votacion(models.Model):
    id=models.AutoField(primary_key=True)    
    jurado=models.IntegerField(verbose_name='jurado')
    degustador=models.IntegerField(verbose_name='degustador')
    muestra=models.IntegerField(verbose_name='muestra')      
    vista_limpidez=models.IntegerField(choices=ESTADOS_VISTA_LIMPIDEZ,default=1)
    vista_color=models.IntegerField(choices=ESTADOS_VISTA_COLOR,default=1)
    olfato_intensidad=models.IntegerField(choices=ESTADOS_OLFATO_INTENSIDAD,default=1)
    olfato_franqueza=models.IntegerField(choices=ESTADOS_OLFATO_FRANQUEZA,default=1)
    olfato_calidad=models.IntegerField(choices=ESTADOS_OLFATO_CALIDAD,default=1)
    gusto_intensidad=models.IntegerField(choices=ESTADOS_GUSTO_INTENSIDAD,default=1)
    gusto_franqueza=models.IntegerField(choices=ESTADOS_GUSTO_FRANQUEZA,default=1)
    gusto_calidad=models.IntegerField(choices=ESTADOS_GUSTO_CALIDAD,default=1)
    gusto_persistencia=models.IntegerField(choices=ESTADOS_GUSTO_PERSISTENCIA,default=1)
    apreciacion_global=models.IntegerField(choices=ESTADOS_APRECIACION_GLOBAL,default=1)
    observaciones=models.TextField(null=True, verbose_name='Observaciones')

    def __str__(self):
        return self.nombre