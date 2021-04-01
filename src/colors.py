
def colours_list(color_busqueda):
	'''Muestra una lista de los colores que genera pygame'''
	
	import pygame #Borrar cuando se importe
				  # BORRAR!!!! DELETE!!!! to import.

	colour_names = pygame.colordict.THECOLORS.items()
	# colour_names.sort(key=lambda name: name[0]) # Sort list by colour name

	for color in colour_names:
		print(color)

colours_list('aliceblue')