import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import time
import customtkinter


'''
Luego de presionar el botón 'Iniciar',se disparara ; un temporizador de una función que haga visible los tres botones ocultos. 
Se deberá calcular e informar la cantidad de segundos transcurridos desde que estos botones se hicieron visibles hasta el momento 
que el usuario logró pulsar todos los botones. 

Continuando con el ejercicio anterior, se deberán incorporar los siguientes mensajes. 
    *si tardo menos de 1 segundo :"Usted es Flash". 
    *si tardo entre 1 y 2 segundos :"Bien ahí". 
    *si tardo entre 2 y 3 segundos :"Medio lenteja". 
    *si tardo más de 3 segundos :"¿Te quedaste dormido?".
    
Luego de informar el tiempo reiniciar el juego.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.btn_oculto_1 = customtkinter.CTkButton(master=self, text="Boton Oculto 1", command=self.btn_oculto_1_on_click)
        self.btn_oculto_2 = customtkinter.CTkButton(master=self, text="Boton Oculto 2", command=self.btn_oculto_2_on_click)
        self.btn_oculto_3 = customtkinter.CTkButton(master=self, text="Boton Oculto 3", command=self.btn_oculto_3_on_click)

        self.flag_btn_1 = False
        self.flag_btn_2 = False
        self.flag_btn_3 = False

        self.tiempo_inicial = 0

    def btn_mostrar_on_click(self):
        if(self.flag_btn_1 == False and self.flag_btn_2 == False and self.flag_btn_3 == False):
            self.activar_boton_oculto()
        else:
            self.btn_check_all_press()   
    
    def btn_oculto_1_on_click(self):
        self.flag_btn_1 = True
        if(self.flag_btn_1 == True and self.flag_btn_2 == True and self.flag_btn_3 == True):
            self.btn_check_all_press()

    def btn_oculto_2_on_click(self):
        self.flag_btn_2 = True
        if(self.flag_btn_1 == True and self.flag_btn_2 == True and self.flag_btn_3 == True):
            self.btn_check_all_press()

    def btn_oculto_3_on_click(self):
        self.flag_btn_3 = True
        if(self.flag_btn_1 == True and self.flag_btn_2 == True and self.flag_btn_3 == True):
            self.btn_check_all_press()
            
    def btn_check_all_press(self):
        ts_fin= time.time()
        tiempo_de_juego= int(ts_fin - self.ts_inicio)
        if(tiempo_de_juego <=1):
            postmensaje ="Usted es Flash"
        elif(tiempo_de_juego > 1 and tiempo_de_juego <=2):
            postmensaje ="Bien ahí"
        elif(tiempo_de_juego > 2 and tiempo_de_juego <=3):
            postmensaje ="Medio lenteja"
        else:
            postmensaje = "¿Te quedaste dormido?"

        mensaje= "su tiempo fue {:.2f}. {}".format(tiempo_de_juego,postmensaje)
        alert(title="fin del juego", message=mensaje)
            
    def activar_boton_oculto(self):
        self.btn_oculto_1.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_oculto_2.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_oculto_3.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.ts_inicio= time.time()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()