import pandas as pd

### RUN PROGRAM FROM Abfrage.py ###############################################

### constants #################################################################
# colors
bgESP = '#FFCCCC'     # background color Spanish
bgFRA = '#CCCCFF'     # background color French
bgITA = '#CCFFCC'     # background color Italian
bgFrame = 'gray'

# define waiting time
waitIncorrect = 700     # time in ms if input was false
waitShowSolution = 2000    # time in ms that correct solution is displayed

# websites from which conjugations are downloaded when adding a new verb
# this only works for french and spanish
# pons does not have conjugation tabels for italian
websiteESP = 'https://de.pons.com/verbtabellen/spanisch/'
websiteFRA = 'https://de.pons.com/verbtabellen/franz%C3%B6sisch/'
websiteITA = ''

# CSV files in which verbs and persons are stored
nameESP = 'SpanischeVerben.csv'
nameFRA = 'FranzoesischeVerben.csv'
nameITA = 'ItalienischeVerben.csv'
PpESP = 'SpanischePersonalpronomen.csv'
PpFRA = 'FranzoesischePersonalpronomen.csv'
PpITA = 'ItalienischePersonalpronomen.csv'

# special characters that can occur in french and spanish verbs
# needed to find new verbs on pons website
umlt = ['ñ', 'é', 'ú', 'í', 'á', 'ü', 'ê', 'è', 'î', 'æ', 'ç']
urlUmlt = ['%C3%B1', '%C3%A9', '%C3%BA', '%C3%AD', '%C3%A1', '%C3%BC',
           '%C3%AA', '%C3%A8', '%C3%AE', '%C3%A6', '%C3%A7']

###############################################################################
# initialization of lists and dataframes that are changed constantly
fName = ''
namePp = ''
website = ''
path = ''

verbs = []
tenses = []
persons = []
selectedVerbs = []

df = pd.DataFrame()
p = pd.DataFrame()
