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
        Converte cada conjunto de coordenadas UTM (x, y) dentro da lista, para
        coordenadas geograficas (latitude, longitude)

        Parameters
        ----------
        listUTM : LIST
            O parametro da funcao deve ser uma lista de lista contendo em cada
            item da lista o par de coortenadas UTM a serem convertidas
            [[UTMx, UTMy], [UTMx, UTMy], ... , [UTMx, UTMy]]

        Returns
        -------
        LIST [(lat, lon),(lat, lon), ... , (lat, lon)]
            Retorna uma lista de tuplas, contendo em cada tupla o par de
            coordenadas convertidas em latitude e longitude.

        """
        
        for coord in listUTM:
            pass
        