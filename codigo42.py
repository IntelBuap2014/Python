#! /usr/bin/python3
# -*- coding:utf-8 -*-
# funcion format() con diccionarios
capitales_paises = {"Mexico":"Df",
		"EU":"Washington",
		"Canada":"Ottawa",
		"Alemania":"Berlin",
		"Francia":"Paris",
		"Inglaterra":"Londres",
		"Autria":"Vienna",
		"Rusia":"Moscu"}
print ("Las capitales son:")
for nombre in capitales_paises:
	print ("{pais:10} -> {capital}".format(pais=nombre, capital=capitales_paises[nombre]))
