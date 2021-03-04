import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb    
from tkinter import scrolledtext as st  

import libros 

class Orden:
    def __init__(self):
        self.libro=libros.Libro()                  
        self.window1=tk.Tk()                              
        self.window1.title('Ordenar Libros')    
        self.notebook1 = ttk.Notebook(self.window1)
        self.load_clients()
        self.libros_dispo()
        self.ordenarr()
        self.allordenes()         
        self.notebook1.grid(column=0, row=0, padx=10, pady=10)
        self.window1.mainloop()

    def load_clients(self):
        self.pagina1 = ttk.Frame(self.notebook1)                            
        self.notebook1.add(self.pagina1, text="Registro Cliente")

        #Titulo Pestaña
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Registrar Datos")
        self.labelframe1.grid(column=0, row=0, padx=50, pady=10)

        #DOCUMENTO
        self.label1 = ttk.Label(self.labelframe1, text="Documento: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.documentload = tk.StringVar() 
        self.entrydocument = ttk.Entry(self.labelframe1, textvariable=self.documentload) 
        self.entrydocument.grid(column=1, row=0, padx=4, pady=4)

        #NOMBRES
        self.label2 = ttk.Label(self.labelframe1, text="Nombres: ")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.chargenombres = tk.StringVar()   
        self.entrynombres = ttk.Entry(self.labelframe1, textvariable=self.chargenombres)
        self.entrynombres.grid(column=1, row=1, padx=4, pady=4)

        #APELLIDOS
        self.label3 = ttk.Label(self.labelframe1, text="Apellidos: ")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.chargeapellidos = tk.StringVar()   
        self.entryapellidos = ttk.Entry(self.labelframe1, textvariable=self.chargeapellidos)
        self.entryapellidos.grid(column=1, row=2, padx=4, pady=4)

        #DIRECCION
        self.label4 = ttk.Label(self.labelframe1, text="Direccion: ")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.chargedireccion = tk.StringVar()   
        self.entrydireccion = ttk.Entry(self.labelframe1, textvariable=self.chargedireccion)
        self.entrydireccion.grid(column=1, row=3, padx=4, pady=4)

        #CIUDAD
        self.label5 = ttk.Label(self.labelframe1, text="Ciudad residencia: ")
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.chargeciudad = tk.StringVar()   
        self.entryciudad = ttk.Entry(self.labelframe1, textvariable=self.chargeciudad)
        self.entryciudad.grid(column=1, row=4, padx=4, pady=4)

        #CODIGO
        self.label6 = ttk.Label(self.labelframe1, text="Codigo Postal: ")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.chargecodigo = tk.StringVar()   
        self.entrycodigo = ttk.Entry(self.labelframe1, textvariable=self.chargecodigo)
        self.entrycodigo.grid(column=1, row=5, padx=4, pady=4)

        #BOTON
        self.boton1 = ttk.Button(self.labelframe1, text="Registrar", command=self.add)
        self.boton1.grid(column=0, row=6, columnspan=2, padx=70, pady=5)

    def add(self):
        datos = (self.documentload.get(), self.chargenombres.get(), self.chargeapellidos.get(), self.chargedireccion.get(), self.chargeciudad.get(), self.chargecodigo.get())
        yes1 = self.libro.insert(datos)
        if yes1 == True:
            mb.showinfo("Información", "Los datos cargaron correctamente")
        else:
            mb.showerror("Alerta!!" , 'No se pudo cargar los datos')

        #Limpiamos los campos
        self.documentload.set("")
        self.chargenombres.set("")
        self.chargeapellidos.set("")
        self.chargedireccion.set("")
        self.chargeciudad.set("")
        self.chargecodigo.set("")    


    def libros_dispo(self):
        self.pagina2 = ttk.Frame(self.notebook1)
        self.notebook1.add(self.pagina2, text="Libros Disponibles")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Libros")
        self.labelframe2.grid(column=0, row=0, padx=50, pady=10)

        self.boton1=ttk.Button(self.labelframe2, text="Listado de libros disponibles", command=self.to_list)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe2, width=28, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def to_list(self):
        answer = self.libro.retrieve_all() 
        self.scrolledtext1.delete("1.0", tk.END) 
        for fila in answer: 
            self.scrolledtext1.insert(tk.END, "Codigo: "+str(fila[0])+"\nTitulo:"+str(fila[1])+"\nAutor:"+str(fila[2])+"\nGenero:"+str(fila[3])+"\nPrecio:"+str(fila[4])+"\n\n")    

    def ordenarr(self):
        self.pagina3 = ttk.Frame(self.notebook1)
        self.notebook1.add(self.pagina3, text="Ordenar Libro")

        #TITULO PESTAÑA
        self.labelframe2 = ttk.LabelFrame(self.pagina3, text="Ordenar")
        self.labelframe2.grid(column=0, row=0, padx=50, pady=10)

        #DOCUMENTO ORDEN
        self.label7 = ttk.Label(self.labelframe2, text="Documento: ")
        self.label7.grid(column=0, row=0, padx=4, pady=4)
        self.documentloadorden = tk.StringVar() 
        self.entrydocumentorden = ttk.Entry(self.labelframe2, textvariable=self.documentloadorden) 
        self.entrydocumentorden.grid(column=1, row=0, padx=4, pady=4)

        #CODIGO LIBRO
        self.label8 = ttk.Label(self.labelframe2, text="Libros: ")
        self.label8.grid(column=0, row=1, padx=4, pady=4)
        self.chargecodigolibro = tk.StringVar()   
        self.entrycodigolibro = ttk.Entry(self.labelframe2, textvariable=self.chargecodigolibro)
        self.chargecodigolibro = ttk.Combobox(self.labelframe2)
        self.chargecodigolibro.grid(column=1, row=1, padx=2, pady=2)
        self.chargecodigolibro['values'] = ('1 - Edipo Rey ','2 -  La flecha negra','3 - Robbie y otros relatos', '4 - Relatos espectrales', '5 - Madame Bovary')
        self.chargecodigolibro.current(0)
        


        #BOTON
        self.boton2 = ttk.Button(self.labelframe2, text="Ordenar", command=self.addord)
        self.boton2.grid(column=0, row=3, columnspan=2, padx=70, pady=5)

    def addord(self):
        datos = (self.documentloadorden.get(), self.chargecodigolibro.get())
        yes = self.libro.insert_ord(datos)
        if yes == True:
            mb.showinfo("Información!!", "Los datos cargaron correctamente")
        else:
            mb.showerror("Alerta!!" , 'No se puede registrar la orden\nDatos incorrectos\n\nVerifique de nuevo')

        #Limpiamos los campos
        self.documentloadorden.set("")
        self.chargecodigolibro.set("")

    def allordenes(self):
        self.pagina4 = ttk.Frame(self.notebook1)
        self.notebook1.add(self.pagina4, text="Ordenes")
        self.labelframe3=ttk.LabelFrame(self.pagina4, text="Ordenes Realizadas")
        self.labelframe3.grid(column=0, row=0, padx=50, pady=10)

        self.boton1=ttk.Button(self.labelframe3, text="Listado de ordenes", command=self.to_list_ordenes)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext2=st.ScrolledText(self.labelframe3, width=37, height=10)
        self.scrolledtext2.grid(column=0,row=1, padx=10, pady=10)

    def to_list_ordenes(self):
        answer = self.libro.retrieve_all_ordenes() 
        self.scrolledtext2.delete("1.0", tk.END) 
        for fila in answer: 
            self.scrolledtext2.insert(tk.END, "Numero Orden: "+str(fila[0])+"\nDocumento: "+str(fila[1])+"\nNombres: "+str(fila[2])+"\nApellidos: "+str(fila[3])+"\nNombre Libro: "+str(fila[4])+"\nAutor Libro: "+str(fila[5])+"\nPrecio Libro: "+str(fila[6])+"\nFecha Orden: "+str(fila[7])+"\n\n")       


app = Orden()