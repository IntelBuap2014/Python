#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Iniciando con las excepciones
while True:
	try:
		numero = int(input("Ingresa un numero: \n"))
		break
	except (ValueError, EOFError, KeyboardInterrupt):
		print ("Ooop! Atrape un excepcion")
