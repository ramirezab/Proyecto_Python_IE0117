import tkinter as tk

class ingresar_nombre():
  def __init__(self):
        self.root = tk.Tk()

        self.var_texto = tk.StringVar()
        self.var_lbl = tk.StringVar()

        self.mi_label = tk.Label(self.root, textvariable=self.var_lbl)
        self.var_lbl.set("Ingresa Tu nombre") # Contenido inicial del Lable
        self.mi_label.grid(row=0, column=0, columnspan=3)

        self.cuadro_texto = tk.Entry(self.root, textvariable=self.var_texto)
        self.cuadro_texto.grid(row=1, column=0, columnspan=2)

        self.btn_aceptar = tk.Button(self.root, text="Aceptar", command=self.aceptar)
        self.btn_aceptar.grid(row=1, column=2)
        
        self.root.mainloop()

      
      
  def aceptar(self):
      
    n = self.var_texto.get()  # Obtenemos el número de la StringVar
      
           
    self.root.quit()
    return n              

