'''
Created on Nov 22, 2012

@author: amilano
'''

from django.db import models

class Juego(models.Model):
    ciudad = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)
    inning = models.CharField(max_length=200)
    visitante = models.CharField(max_length=200)
    v_carreras = models.IntegerField()
    v_hits = models.IntegerField()
    v_errores = models.IntegerField()
    homeclub = models.CharField(max_length=200)
    h_carreras = models.IntegerField()
    h_hits = models.IntegerField()
    h_errores = models.IntegerField()
    fecha = models.DateTimeField('dia del juego')
    parse_id = models.CharField(max_length=200)
    
    