import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random
import time


'''
Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado
 el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “usted es un Psíquico”.
	2° intento: “excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	Más de 6 intentos: “afortunado en el amor!!”.

de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Reset", command=self.btn_reset_on_click)
        self.btn_mostrar.grid(row=3, pady=20, columnspan=2, sticky="nsew")

        self.iniciar_juego()

    def iniciar_juego(self):
        self.numero_secreto = random.randrange(1, 100)
        self.numero_intento = 0
        print(self.numero_secreto)
        self.flag_playing = True
        self.ts_inicio_juego = time.time()

    def btn_reset_on_click(self):
        self.iniciar_juego()

    def btn_mostrar_on_click(self):
        if(self.flag_playing):
            numero_ingresado = int(self.txt_numero.get())
            self.numero_intento = self.numero_intento + 1
            if(numero_ingresado == self.numero_secreto):
                ts_fin_tiempo = time.time()
                tiempo_juego = ts_fin_tiempo - self.ts_inicio_juego
                # match(self.numero_intento):
                #     case 1:
                #         premensaje = "Usted es un Psíquico"
                #     case 2:
                #         premensaje = "Excelente percepción"
                #     case 3:
                #         premensaje = "Esto es suerte"
                #     case 4 | 5 | 6:
                #         premensaje = "Excelente técnica"
                #     case _:
                #         premensaje = "Afortunado en el amor!!"
                # mensaje = "{0} - Ganaste en {1}".format(premensaje,self.numero_intento)
                self.flag_playing = False
            elif(numero_ingresado > self.numero_secreto):
                #cantidad= int(numero_ingresado)-int(self.numero_secreto)
                mensaje = "Te pasaste" 
            else:
                #cantidad = int(self.numero_secreto)-int(numero_ingresado)
                mensaje = "Te faltan"
            alert(title="Resultado", message=mensaje)


if __name__ == "__main__":
    app = App()
    app.mainloop()