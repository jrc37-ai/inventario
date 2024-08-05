import tkinter as tk
from tkinter import font
from config import *
import util.util_ventana as util_ventana


class FormMasterDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Tienda')
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)
    
    def paneles(self):
        # Creación de paneles (barra superior, menú lateral y cuerpo principal)
        self.barra_superior = tk.Frame(self, bg = COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        self.labelTitulo = tk.Label(self.barra_superior, text='Tienda')
        self.labelTitulo.config(fg='#fff',
                                font=("Helvetica", 15),
                                bg=COLOR_BARRA_SUPERIOR,
                                pady=10,
                                width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        self.labelTitulo = tk.Label(self.barra_superior, text='e-mail')
        self.labelTitulo.config(fg='#fff',
                                font=("Helvetica", 10),
                                bg=COLOR_BARRA_SUPERIOR,
                                padx=20)
        self.labelTitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 13
        alto_menu = 2

        self.buttonDashBoard = tk.Button(self.menu_lateral)
        self.buttonProfile = tk.Button(self.menu_lateral)
        self.buttonPicture = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)
        self.buttonSettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Dashboard", self.buttonDashBoard),
            ("Profile", self.buttonProfile),
            ("Picture", self.buttonPicture),
            ("Info", self.buttonInfo),
            ("Settings", self.buttonSettings)
        ]

        for text, button in buttons_info:
            self.configurar_boton_menu(button, text, ancho_menu, alto_menu)
        
    def configurar_boton_menu(self, button, text, ancho_menu, alto_menu):
        button.config(text=text,
                      anchor="e",
                      font=('Helvetica', 12, 'bold'),
                      bd=0,
                      bg=COLOR_MENU_LATERAL,
                      fg='white',
                      width=ancho_menu,
                      height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)
    
    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
    
    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')
    
    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')