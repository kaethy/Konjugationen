from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont

import variables

### RUN PROGRAM FROM Abfrage.py ###############################################

### define GUI ################################################################
root = Tk()
root.wm_title("Konjugationstrainer")
helv20 = tkFont.Font(family='Helvetica', size=20)
helv12 = tkFont.Font(family='Helvetica', size=12)
helv12F = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
n = ttk.Notebook(root)
n.pack(padx=20, pady=20)
f0 = Frame(n)   # language selection
f1 = Frame(n)   # first page (main menu for one language)
f2 = Frame(n)   # second page (vocabulary quiz)
n.add(f0, text='Sprache')
n.add(f1, text='Auswahl')
n.add(f2, text='Abfrage')

### Tab Management of Verbs ###################################################
# verbs
fraV = Frame(f1, relief="flat", width=100, height=100, bd=1)
scbV = Scrollbar(fraV, orient="vertical")
lbxV = Listbox(fraV, font=helv12, width=15,
               height=20, selectmode="multiple",
               yscrollcommand=scbV.set, exportselection=0)
scbV["command"] = lbxV.yview
[lbxV.insert("end", v) for v in variables.verbs]
fraV.grid(row=1, column=2, rowspan=4, padx=5, pady=5)
lbxV.pack(side="left")
scbV.pack(side="left", fill="y")
lbxV.configure(justify=CENTER)

# tenses
fraT = Frame(f1, relief="flat", width=100, height=400, bd=1)
scbT = Scrollbar(fraT, orient="vertical")
svTenses = StringVar(value=tuple(variables.tenses))
lbxT = Listbox(fraT, font=helv12, width=25,
               height=20, selectmode="multiple",
               listvariable=svTenses, yscrollcommand=scbT.set,
               exportselection=0)
scbT["command"] = lbxT.yview
fraT.grid(row=1, column=3, rowspan=4, padx=5, pady=5)
lbxT.pack(side="left")
scbT.pack(side="left", fill="y")
lbxT.configure(justify=CENTER)

### Tab Quiz ##################################################################
lblVerb = ttk.Label(f2, text="Verb", width=20, font=helv12F,
                    background=variables.bgFrame)
lblVerb.grid(row=1, column=2, padx=5, pady=(100, 5),
             sticky=(E, W))


lblTense = ttk.Label(f2, text="Zeit", width=20, font=helv12,
                     background=variables.bgFrame)
lblTense.grid(row=2, column=2, padx=5, pady=(5, 5),
              sticky=(E, W))

lblPerson = ttk.Label(f2, text="Person", width=20, font=helv12,
                      background=variables.bgFrame)
lblPerson.grid(row=3, column=1, padx=20, pady=5)

conjugation = StringVar()
conj_entry = ttk.Entry(f2, width=25, textvariable=conjugation,
                       font=helv20)
conj_entry.grid(row=3, column=2, sticky=(E, W))

### Tab Language Selection ####################################################
languageList = ["Sprache wählen", "Spanisch", "Französisch", "Italienisch"]
style = ttk.Style()
style.configure('my.TMenubutton', font=("Helvetica", "20"))
language = StringVar()
language.set(languageList[0])

# allow changing tabs by clicking on them in the left upper corner
n.enable_traversal()

# start with language selection tab
n.select(f0)
