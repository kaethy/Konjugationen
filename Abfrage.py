# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 18:53:40 2020

@authors: Kathi + Wolfgang
"""
from tkinter import *
from tkinter import ttk
import functions
import gui
import utils

### RUN PROGRAM FROM HERE #####################################################

### GUI preparation ###########################################################
# display window in the center of screen
utils.bring_to_Center()

# First tab: language selection
languageSelect = ttk.OptionMenu(gui.f0, gui.language, *gui.languageList,
                                command=functions.languageSelection,
                                style='my.TMenubutton')
languageSelect['menu'].configure(font=("Helvetica", "20"))
languageSelect.pack(pady=(150, 0))

# Second tab: connect functions to buttons
btnStart = ttk.Button(gui.f1, text="Abfrage starten", width=20,
                      command=functions.start)
btnStart.grid(row=3, column=1, sticky=(N, E, W, S), padx=5, pady=5)
btnAdd = ttk.Button(gui.f1, text="Verb hinzufügen", width=20,
                    command=functions.addVerb)
btnAdd.grid(row=1, column=1, sticky=(N, E, W, S), padx=5, pady=5)
btnDel = ttk.Button(gui.f1, text="Verb löschen", width=20,
                    command=functions.deleteVerb)
btnDel.grid(row=2, column=1, sticky=(N, E, W, S), padx=5, pady=5)
btnEnd = ttk.Button(gui.f1, text="Ende", width=10,
                    command=functions.end)
btnEnd.grid(row=4, column=1, sticky=(E, W),
            padx=5, pady=5)

# Thrid tab: pressing return key checks whether input was correct
gui.conj_entry.bind("<Return>", functions.test)

# event management to end program
gui.root.protocol("WM_DELETE_WINDOW", functions.end)
gui.root.bind('<Control-c>', functions.quit)

### start main loop ###########################################################
gui.root.mainloop()
###############################################################################
