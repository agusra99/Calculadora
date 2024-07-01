import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('images.ico')
        #Atributos de la clase
        self.expresion = ''
        self.entrada = None
        self.entrada_texto = tk.StringVar()
        self._creacion_componentes()

    def _creacion_componentes(self):
        #frame para caja de texto
        entrada_frame = tk.Frame(self,width=400, height=50,bg='grey')
        entrada_frame.pack(side = tk.TOP)
        entrada = tk.Entry(entrada_frame,font=('arial',18,'bold'), textvariable=self.entrada_texto,width=30, justify = tk.RIGHT)
        entrada.grid(row=0,column=0,ipady=10)

        #frame para parte inferior
        botones_frames = tk.Frame(self,width=400,height=450,bg='grey')
        botones_frames.pack()

        #primer renglon
        boton_limpiar = tk.Button(botones_frames,text = 'C',width='32',height=3,bd=0,bg='#eee',cursor='pirate',command=self._evento_limpiar)
        boton_limpiar.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
        boton_dividir = tk.Button(botones_frames,text ='/',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda: self._evento_click('/')).grid(row=0,column=3,padx=1,pady=1)

        #segundo renglon
        boton_siete = tk.Button(botones_frames,text='7',width=10,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(7)).grid(row=1,column=0,padx=1,pady=1)
        boton_ocho = tk.Button(botones_frames,text='8',width=10,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(8)).grid(row=1,column=1,padx=1,pady=1)
        boton_nueve = tk.Button(botones_frames,text='9',width=10,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(9)).grid(row=1,column=2,padx=1,pady=1)
        boton_multiplicar = tk.Button(botones_frames,text='*',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda: self._evento_click('*')).grid(row=1,column=3,padx=1,pady=1)

        #tercer renglon
        boton_cuatro = tk.Button(botones_frames,text='4',width=10,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(4)).grid(row=2,column=0,padx=1,pady=1)
        boton_cinco = tk.Button(botones_frames,text='5',width=10,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(5)).grid(row=2,column=1,padx=1,pady=1)
        boton_seis = tk.Button(botones_frames,text='6',width=10,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(6)).grid(row=2,column=2,padx=1,pady=1)
        boton_restar = tk.Button(botones_frames,text='-',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda: self._evento_click('-')).grid(row=2,column=3,padx=1,pady=1)

        #cuarto renglon
        boton_uno = tk.Button(botones_frames,text='1',width=10,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(1)).grid(row=3,column=0,padx=1,pady=1)
        boton_dos = tk.Button(botones_frames,text='2',width=10,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(2)).grid(row=3,column=1,padx=1,pady=1)
        boton_tres = tk.Button(botones_frames,text='3',width=10,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(3)).grid(row=3,column=2,padx=1,pady=1)
        boton_sumar = tk.Button(botones_frames,text='+',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda: self._evento_click('+')).grid(row=3,column=3,padx=1,pady=1)

        #quinto renglon
        boton_cero = tk.Button(botones_frames,text = '0',width=21,height=3,bd=0,bg='#fff',cursor='gobbler',command=lambda: self._evento_click(0)).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
        boton_punto = tk.Button(botones_frames,text='.',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda: self._evento_click('.')).grid(row=4,column=2,padx=1,pady=1)   
        boton_evaluar = tk.Button(botones_frames,text='=',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda: self._evento_evaluar()).grid(row=4,column=3,padx=1,pady=1)   

    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self,elemento):
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

    def _evento_evaluar(self):
        #eval evalua la expresion str como una expresion aritmetica
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error',f'Ocurrió un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()