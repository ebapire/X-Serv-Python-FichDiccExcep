#!/usr/bin/python
# -*- coding: utf-8 -*-

# hola, hola

fd = open('/etc/passwd', 'r')

lineas = fd.readlines()
fd.close()

lista_usuarios = {}
for linea in lineas:
    elementos = linea.split(':')
    lista_usuarios[elementos[0]] = elementos[-1][:-1]

print "root: " + lista_usuarios['root']
try:
    print "Imaginario: " + lista_usuarios['imaginario']
except KeyError:
    print "usuario incorrecto"