'''
    This is Class to create GUI
'''

import tkinter as tk
import os
# https://teratail.com/questions/88956

class GUI:
    def __init__(self, title):
        # Make base
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry('1300x650')

    def frame(self):
        # create frame
        return tk.Frame()

    def label(self, frame, text='text', side='TOP'):
        # create a label
        lb = tk.Label(frame, text=text)
        self.pack(lb, side)

    def text(self, frame, height=1, width=140, side='TOP'):
        # create text box
        tx = tk.Text(frame, height=height, width=width)
        tx.config(state='disabled', bg='#dddddd')
        self.pack(tx, side)
        return tx

    def button(self, frame, func, text='text', side='TOP'):
        # create button
        btn = tk.Button(frame, text=text, command=func)
        self.pack(btn, side=side)

    def pack(self, smt, side='TOP'):
        # pack label, text box, button
        if side.upper() == 'TOP':
            smt.pack()
        elif side.upper() == 'LEFT':
            smt.pack(side=tk.LEFT)

    def end(self):
        self.root.mainloop()

    
