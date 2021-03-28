#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


class Persona():
	'''Este documento trata de especificar la descripcion de 'Persona', con 
	ciertas caracteristicas que lo hacer ser como lo que es.'''
	def __init__(self, nombre, apellidos, sexo, edad, identificacion):
		''' Constructor de la Clase persona '''
		self.nombre = nombre
		self.apellidos = apellidos
		self.sexo = sexo
		self.edad = edad
		self.identificacion = identificacion

	def __str__(self):
		'''Devuelte una descripcion representatica de persona

		'''
		return "%s Mi nombre es %s %s soy %s, tengo %i años. \nMi identifica'\
		'ion es: %s" % (self.__doc__[25:34], self.nombre, self.apellidos,
				self.get_genero(self.sexo), self.edad, self.identificacion)

	def hablar(self, mensaje):
		''' La persona devuelve un mesaje y lo escribe en la consola. '''
		return mensaje

	def get_genero(self, sexo):
		''' Mostrar el genero de Persona '''
		sexo = ('Hombre', 'Mujer')
		if self.sexo.lower() == 'h':
			return sexo[0]
		elif self.sexo.lower() == 'f':
			return sexo[1]
		else:
			'Desconocido'

	def get(self):
		''' Toma algunas caracteristicas para agregar a persona '''
		return self.nombre + ', ' + self.sexo + ', '+ str(self.edad)

	def muestra(self):
		'''Muestra informacion especifica de la persona.
		los datos devueltos por este metodo son mas largos de 79 caracteres 
		sobre la linea y deben acortarse respecto a la guia de estilos de PEP
		'''
		return 'Hola soy '+self.nombre+' un '+self.sexo+', tengo '
		+str(self.edad)+' años. \nMi CURP es: '+self.identificacion


class Trabajador(Persona):
	'''Este documento trata de especificar la descripcion de un 'Trabajador', 
	con ciertas caracteristicas que lo hacer ser como lo que es.'''
	def __init__(self, nombre, apellidos, sexo, edad, identificacion,
				 ocupacion, nivel_academico, nombre_carrera, salario, 
				 nombre_empresa):

		Persona.__init__(self, nombre, apellidos, sexo, edad, identificacion)

		self.ocupacion = ocupacion
		self.nivel_academico = nivel_academico
		self.nombre_carrera = nombre_carrera
		self.salario = salario
		self.metas_de_trabajo = ['nuevo', 'junior', 'academia', 'contratado']
		self.nombre_empresa = nombre_empresa

	def __str__(self):
		''' Por ahora no se muestra nada del Trabajador '''
		return '%s %s esta trabajando en %s, su salario es $%i por sus entudi'\
		'os en %s.' % (self.nombre, self.apellidos, self.nombre_empresa,
					self.salario, self.nivel_academico)

	def consulta_tareas(self):
		''' Muestra las tareas que el trabajador ya cumplio '''
		return ', ' + join(self.metas_de_trabajo)



class Clase():
	'''Clase de ejemplo '''
	def __init__(self, parametro):
		''' Iniciando los atributos de la clase Clase'''
		self.atributo = parametro

	def metodo(self, parametroMetodo):
		''' Ejemplo del primer metodo de Clase'''
		self.atributoMetodo = parametroMetodo
		return self.atributoMetodo

	def get_metodo():
		'''Metodo para obtener datos'''
		pass

	def set_metodo():
		'''Metodo para mostrar o devolver datos.'''
		pass


# clase = Clase()

mau_trabaja = Trabajador("Mauricio", 'Torres Garcia', 'H', 35,
			"TOGM850328HDFRRR04", 'Programador', 'Universidad',
			"Ciencias de la computacion", 35000, 'Mecaro')



print ("Hola")