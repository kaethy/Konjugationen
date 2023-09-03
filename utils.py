import pandas as pd

from tkinter import *
import tkinter as tk

import variables
import gui

### RUN PROGRAM FROM Abfrage.py ###############################################

### helper functions ##########################################################


def addVerbToCsv(seriesNewVerb, newVerb):
    variables.df = pd.concat([variables.df, seriesNewVerb.to_frame().T],
                             verify_integrity=True)
    variables.verbs = variables.verbs + [newVerb]
    variables.df.to_csv(variables.fName)

# bring window to center of screen


def bring_to_Center():
    gui.root.lower()  # brings window to back
    gui.root.update_idletasks()  # actualize window
    # get height and width
    w = gui.root.winfo_width()
    h = gui.root.winfo_height()
    # get size of screen
    screenWidth = gui.root.winfo_screenwidth()
    screenHeigth = gui.root.winfo_screenheight()

    x = (screenWidth/2) - (w/2)
    y = (screenHeigth/2) - (h/2)
    gui.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    gui.root.lift()


def changeColor(color, text):
    gui.conj_entry.config(foreground=color)
    gui.conjugation.set(text)


def changeBackgroundColor():
    gui.f2.config(bg=variables.bgFrame)  # '#RRGGBB' #FFAAAA
    gui.lblPerson['background'] = variables.bgFrame
    gui.lblVerb['background'] = variables.bgFrame
    gui.lblTense['background'] = variables.bgFrame


def displayCorrectInput(input):
    # mark input green for a short time
    gui.root.after(0, changeColor, "green", input)
    gui.root.after(variables.waitIncorrect, changeColor, "black", '')


def displayIncorrectInput(input, solution):
    # mark input red, then display correct solution in green
    gui.root.after(0, changeColor, "red", input)
    gui.root.after(variables.waitIncorrect, changeColor, "green", solution)
    gui.root.after(variables.waitIncorrect+variables.waitShowSolution,
                   changeColor, "black", '')


def displayFirstVerb():
    gui.lblVerb.config(text=variables.selectedVerbs[0][1])
    gui.lblTense.config(text=variables.selectedVerbs[0][2])
    gui.lblPerson.config(text=variables.selectedVerbs[0][0])
    gui.conj_entry.focus_force()


def displayNextVerb(wait):
    gui.root.after(wait, showElement, gui.lblVerb,
                   variables.selectedVerbs[0][1])
    gui.root.after(wait, showElement, gui.lblTense,
                   variables.selectedVerbs[0][2])
    gui.root.after(wait, showElement, gui.lblPerson,
                   variables.selectedVerbs[0][0])
    gui.conj_entry.focus_get()


def fillListboxes():
    lenVerbs = len(variables.verbs)
    lenTenses = len(variables.tenses)
    gui.lbxV.delete(first=0, last=lenVerbs-1)
    [gui.lbxV.insert("end", v) for v in variables.verbs]
    gui.lbxT.delete(first=0, last=lenTenses-1)
    [gui.lbxT.insert("end", t) for t in variables.tenses]


def endQuiz(wait):
    gui.root.after(wait, showElement, gui.lblVerb, 'Verb')
    gui.root.after(wait, showElement, gui.lblTense, 'Zeit')
    gui.root.after(wait, showElement, gui.lblPerson, 'Person')
    gui.root.after(wait, gui.n.select, gui.f1)


def evaluateInput(input, solution):
    if (input == solution):
        variables.selectedVerbs = variables.selectedVerbs[1:]
        displayCorrectInput(input)
        wait = variables.waitIncorrect
    else:
        variables.selectedVerbs = variables.selectedVerbs[1:] + \
            [variables.selectedVerbs[0]]  # ask verb again in the end
        displayIncorrectInput(input, solution)
        wait = variables.waitIncorrect+variables.waitShowSolution
    gui.conjugation.set("")
    return wait

# get conjugations of verb from pons website


def getConjOf(verb):
    # get tables
    conTab = pd.read_html(str(variables.website + removeUmlt(verb)))
    # list of strings of dataframe
    cons = [list(removeQue(k).loc[:, 1:].values)
            for k in conTab[:len(variables.tenses)]]
    res = [[' '.join(s).replace(' | ', '/') for s in k] for k in cons]
    return res


def getLanguageVariables():
    if (gui.language.get() == gui.languageList[1]):
        variables.fName = variables.path+variables.nameESP
        variables.namePp = variables.path+variables.PpESP
        variables.bgFrame = variables.bgESP
        variables.website = variables.websiteESP
    elif (gui.language.get() == gui.languageList[2]):
        variables.fName = variables.path+variables.nameFRA
        variables.namePp = variables.path+variables.PpFRA
        variables.bgFrame = variables.bgFRA
        variables.website = variables.websiteFRA
    else:
        variables.fName = variables.path+variables.nameITA
        variables.namePp = variables.path+variables.PpITA
        variables.bgFrame = variables.bgITA
        variables.website = variables.websiteITA


def loadCSVFiles():
    variables.df = pd.read_csv(variables.fName, index_col=0, header=0)
    variables.df = variables.df.applymap(eval)
    variables.p = pd.read_csv(variables.namePp, header=None)
    variables.verbs = variables.df.index.tolist()
    variables.tenses = variables.df.columns.tolist()
    variables.persons = variables.p.values.flatten().tolist()


def prepareSelectedVerbs(verbs, tenses):
    variables.selectedVerbs = []
    for v in verbs:
        for z in tenses:
            for p in range(6):
                variables.selectedVerbs.append([variables.persons[p],
                                                variables.verbs[v],
                                                variables.tenses[z],
                                                variables.df.iloc[v, z][p]])


def showElement(element, txt):
    element.config(text=txt)

# adaptation necessary to read french verbs


def removeQue(arg):
    if (len(arg.iloc[0]) == 1):  # FRE double Impératif entries
        arg[1] = arg[0]
        return arg
    if (arg.iloc[0, 0] == 'que'):  # FRE delete que column for Subjonctif
        return arg.iloc[:, 1:]
    else:
        return arg


def removeUmlt(verb):
    for u, U in zip(variables.umlt, variables.urlUmlt):
        verb = verb.replace(u, U)
    return verb


def removeVerbFromCsv(verb2Delete):
    variables.df.drop(verb2Delete)
    variables.verbs.remove(verb2Delete)
    variables.df.to_csv(variables.fName)
