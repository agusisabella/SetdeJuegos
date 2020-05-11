import hangman
import reversegam
import PySimpleGUI as sg
import json
import os
import csv

#import tictactoeModificado


def main(args):
	nombreArch='archivoJugadoresNuevo.csv'
	def imprimir(data):
		pass
	def MostrarJugadores():
		try:
			with open('archivoJugadoresNuevo.csv', newline='') as csvfile:
				reader = csv.DictReader(csvfile)
				sg.Print('NOMBRE         EDAD ', do_not_reroute_stdout=False)
				for row in reader:
					print(row["nombre"], row["edad"],row["juego"])

		except:
			sg.popup('No se encontraron jugadores :( )' )


	#--------------------PRIMER INTERFACE----------
	#------------------INGRESAR DATOS JUGADOR----
	layout = [  [sg.Text('HOLA. vamos a jugar!!')],
            [sg.Text('Tu nombre:', ), sg.InputText(size=(15, 1),key='nombre')],
            [sg.Text('edad:', ), sg.InputText(size=(2,1),key='edad')],
            [sg.Button('JUGAR'), sg.Button('Salir'), sg.Button('Ver Jugadores')  ]]
	window = sg.Window('------JUEGOS----', layout)

	esperando = True

	while esperando:                             # Loop de ingreso de datos
		event,values = window.read()

		if(event=='JUGAR'):
			if (values['nombre'] == ''):
				sg.popup('INGRESE UN NOMBRE PARA PODER JUGAR', )

			elif(values['edad']==''):
				sg.popup('INGRESE UNA EDAD PARA PODER JUGAR', )

			else:
				esperando=False
				window.close()
		elif(event == 'Ver Jugadores'):
			MostrarJugadores()


	#----------------------ELEGIR JUEGO--------------------
	menu= [  [sg.Text('ELIGE UN JUEGO')],
            [ sg.Button('AHORCADO', key='AHORCADO',size=(15, 1))],
            [sg.Button('TA TE TI', size=(15, 1))],
            [sg.Button('OTELLO',size=(15, 1))],
            [sg.Button(' SALIR ',size=(15, 1),button_color=('white', 'firebrick3'))],

        ]
	while not esperando:						#-loop de ingreso de juego
		window = sg.Window('------JUEGOS.py----', menu)
		opcion,valores = window.read()
		window.close()
		if opcion == 'AHORCADO' :
			hangman.main()

		elif opcion == 'TA TE TI':
			tictactoeModificado.main()

		elif opcion == 'OTELLO':
			reversegam.main()

		elif opcion == ' SALIR ':
			esperando=True
		esperando=True
	try:
		if not(os.path.exists(nombreArch)):
			csvfile= open (nombreArch, "x")
			fieldnames = ['nombre', 'edad','juego']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			if(opcion==' SALIR ' ):
				opcion= 'No jugO'
		diccionario={"nombre":values['nombre'],"edad":values['edad'],"juego":opcion}
		with open(nombreArch, 'a', newline='') as csvfile:
			fieldnames = ['nombre', 'edad','juego']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writerow(diccionario)
		sg.popup(' Se guardó la informacion de usuario' )
	except:
		sg.popup('no se pudo guardar la informacion de usuario' )



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
