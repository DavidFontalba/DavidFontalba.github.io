#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author David Galván Fontalba

from tkinter import *
import requests
from tkinter import ttk


class Aplicacion:
    root = Tk()
    # Texto para la cantidad en euros a convertir
    info = Text(root, width=50, height=1, state='disabled')
    # Texto para escribir el resultado
    result = Text(root, width=50, height=1, state='disabled')
    # ComboBox divisa a convertir
    to_convert = ttk.Combobox(root,
                              values=["CAD", "HKD", "ISK", "PHP", "DKK", "HUF", "CZK", "AUD", "RON", "SEK",
                                      "IDR", "INR", "BRL", "RUB", "HRK", "JPY", "THB", "CHF", "SGD", "PLN", "BGN",
                                      "TRY", "CNY", "NOK", "NZD", "ZAR", "USD", "MXN", "ILS", "GBP", "KRW", "MYR"],
                              state='readonly')
    button_list = []

    def __init__(self):

        self.root.geometry('430x350')
        self.root.configure(bg='beige')
        self.root.title('Conversor de euros a otras divisas.')

        self.info.grid(column=0, row=0, padx=10, pady=20, columnspan=3)

        index_column = 0
        index_row = 2
        for i in [7, 8, 9, 4, 5, 6, 1, 2, 3, 0, '.', '<']:
            if i == 7:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(7))
            elif i == 8:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(8))
            elif i == 9:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(9))
            elif i == 4:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(4))
            elif i == 5:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(5))
            elif i == 6:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(6))
            elif i == 1:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(1))
            elif i == 2:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(2))
            elif i == 3:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(3))
            elif i == 0:
                button = ttk.Button(self.root, text=i, command=lambda: self.write(0))
            elif i == '.':
                button = ttk.Button(self.root, text=i, command=lambda: self.write('.'))
            elif i == '<':
                button = ttk.Button(self.root, text=i, command=lambda: self.remove())

            self.button_list.append(button)
            button.grid(column=index_column, row=index_row, padx=5, pady=5)
            if index_column >= 2:
                index_column = 0
                index_row += 1
            else:
                index_column += 1

        # ComboBox para las monedas a convertir
        self.to_convert.grid(column=0, row=6, padx=10, pady=10, columnspan=3)

        # Texto para escribir el resultado
        self.result.grid(column=0, row=7, padx=10, pady=10, columnspan=3)

        # Boton confirmar
        ok_button = ttk.Button(self.root, text='OK', command=lambda: self.calcs())
        ok_button.grid(column=1, row=8, padx=10, pady=15)
        self.root.mainloop()

    def calcs(self):
        self.result.configure(state='normal')
        self.result.delete("1.0", END)
        to_convert_now = self.to_convert.get()

        if to_convert_now != 'EUR':
            url = "https://api.exchangeratesapi.io/latest?symbols=" + to_convert_now
        else:
            print('Debes elegir dos divisas diferentes')
            exit(1)

        # petición al servidor de la API
        respuesta = requests.get(url)

        if respuesta.status_code != 200:
            print("Error ", respuesta.status_code)
            exit(1)

        data = respuesta.json()

        amount = float(self.info.get("1.0", END))

        if to_convert_now != 'EUR':
            change = float(data['rates'][to_convert_now])

        # Hacemos el calculo correspondiente para devolverle la conversión de la cantidad concreta que ha introducido
        # ahora que sabemos cuál es la conversión concreta a hacer.
        converted = amount * change

        self.result.insert("1.0", f'{amount} € son {converted} {to_convert_now}')
        self.result.configure(state='disabled')

    def write(self, valor):
        self.info.configure(state='normal')
        self.info.insert(END, valor)
        self.info.configure(state='disabled')

    def remove(self):
        self.info.configure(state='normal')
        self.info.delete("1.0", END)
        self.info.configure(state='disabled')


def main():
    Aplicacion()
    return


if __name__ == '__main__':
    main()
