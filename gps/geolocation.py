# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:57:24 2020

@author: Ronan Teodoro de Jesus
"""

class Geolocation():
    """Contem as principais funcoes para trabalhar com dados de geolocalizacao,
       incluindo conversao de sistema de coordenadas e dados referente a
       altitudes geograficas.
    """
    
    @classmethod
    def UTM2COORDS(self, listUTM):
        """
        Converte cada conjunto de coordenadas UTM (x, y) dentra da lista, para
        coordenadas geograficas (latitude, longitude)

        Parameters
        ----------
        listUTM : TYPE
            DESCRIPTION.

        Returns
        -------
        list [(lat, lon),(lat, lon), ... , (lat, lon)]

        """
        
        for coord in listUTM:
            pass