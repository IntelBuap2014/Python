#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Lectura de teclado usando eval
numero=eval(input("Ingrese un numero ->\t"))
decimal=eval(input("Ingrese un decimal ->\t"))
cadena=input("Ingrese una cadena ->\t")
complejo=eval(input("Ingrese un complejo ->\t"))
print ("El tipo de Dato ingresado es [%d]" % int(numero))
print ("El tipo de Dato ingresado es [%f]" % float(decimal))
print ("El tipo de Dato ingresado es [%s]" % str(cadena))
print ("El tipo de Dato ingresado es [%s]" % complejo)
