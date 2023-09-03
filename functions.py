import pandas as pd

from tkinter import *
import tkinter as tk
import tkinter.simpledialog

import random
import variables
import gui
import utils

### RUN PROGRAM FROM Abfrage.py ###############################################

### functions connected to buttons ############################################
# preload verbs from csv file according to selection of language


def languageSelection(event):
    # read conjugations
    utils.getLanguageVariables()
    # load verbs, tenses and persons from csv files
    utils.loadCSVFiles()
    # fill listboxes with verbs and tenses of language
    utils.fillListboxes()
    # change color settings
    utils.changeBackgroundColor()

    # switch to second tab
    gui.n.select(gui.f1)

# configure and start quiz


def start():
    # switch to third tab
    gui.n.select(gui.f2)

    s1 = gui.lbxV.curselection()      # verbs
    s2 = gui.lbxT.curselection()      # tenses

    # creates list for quiz
    utils.prepareSelectedVerbs(s1, s2)

    if (len(variables.selectedVerbs) == 0):
        tk.messagebox.showinfo('Fehlermeldung',
                               'Bitte Verben und Zeiten auswählen.')
        return

    # verbs should appear in random order during the quiz
    random.shuffle(variables.selectedVerbs)

    # show first verb of quiz
    utils.displayFirstVerb()

# evaluate input


def test(event):
    input = gui.conjugation.get()
    solution = variables.selectedVerbs[0][3]

    # check input and adapt selected verb forms
    # deletes verb from query list if it was correct
    wait = utils.evaluateInput(input, solution)

    if (len(variables.selectedVerbs) > 0):
        utils.displayNextVerb(wait)
    else:
        utils.endQuiz(wait)

# delete verb from csv file


def deleteVerb():
    verb2Delete = tkinter.simpledialog.askstring(
        "Verb löschen", "Bitte Verb eingeben:", parent=gui.root)
    if (verb2Delete == None):   # break
        return

    # update surface
    pos = variables.verbs.index(verb2Delete)
    gui.lbxV.delete(pos, pos)

    # update CSV file
    utils.removeVerbFromCsv(verb2Delete)

# add verb from pons website to csv file


def addVerb():
    newVerb = tkinter.simpledialog.askstring(
        "Verb hinzufügen", "Bitte Verb eingeben:", parent=gui.root)
    if (newVerb == None):   # break
        return

    try:
        seriesNewVerb = pd.Series(utils.getConjOf(newVerb),
                                  index=variables.tenses, name=newVerb)
    except:
        tk.messagebox.showinfo('Fehlermeldung', 'Verb nicht gefunden!')
        return

    # update CSV file
    try:
        utils.addVerbToCsv(seriesNewVerb, newVerb)
        # update surface
        gui.lbxV.insert("end", newVerb)
    except:
        tk.messagebox.showinfo('Fehlermeldung',
                               'Das Verb ist bereits vorhanden!')


def end():
    gui.root.destroy()


def quit(event):
    print("you pressed control c")
    gui.root.destroy()
