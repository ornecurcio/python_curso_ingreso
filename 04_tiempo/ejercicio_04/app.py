import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
Al presionar el botón INICIAR se debe mostrar un mensaje de 
bienvenida "Bienvenidos a la UTN FRA" cada 2 segundos, 
al mostrar el mensaje 5 veces que se detenga AUTOMÁTICAMENTE.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.btn_cancelar = customtkinter.CTkButton(master=self, text="Cancelar", command=self.btn_cancelar_on_click)
        self.btn_cancelar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.contador  = 0

    def btn_mostrar_on_click(self):
        self.mostrar_mensaje()
        
    def btn_cancelar_on_click(self):
        self.after_cancel(self.id_mostrar_alerta)

    def mostrar_mensaje(self):
        self.contador= self.contador + 1
        mensaje= "Bienvenidos a la UTN FRA, este es el saludo numero {0}".format(self.contador)
        alert(title="", message=mensaje)
        if(self.contador == 5):
            self.after_cancel(self.id_mostrar_alerta)
            print("Se cancelo")
        else:
            self.id_mostrar_alerta = self.after(2000, self.mostrar_mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()