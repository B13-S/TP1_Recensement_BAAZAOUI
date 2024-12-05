import csv
import matplotlib.pyplot as plt

# communes ciblées
communes_immediate = ['Appoigny', 'Auxerre', 'Moneteau', 'Saint-Georges-sur-Baulche']
communes_totale = [
    'Appoigny', 'Augy', 'Auxerre', 'Bleigny-le-Carreau', 'Branches',
    'Champs-sur-Yonne', 'Charbuy', 'Chevannes', 'Chitry', 'Coulanges-la-Vineuse',
    'Escamps', 'Escolives Sainte-Camille', 'Gurgy', 'Gy-l’Evêque', 'Irancy',
    'Jussy', 'Lindry', 'Moneteau', 'Montigny-la-Resle', 'Perrigny', 'Quenne',
    'Saint-Bris-le-Vineux', 'Saint-Georges-sur-Baulche', 'Vallan', 'Venoy',
    'Villefargeau', 'Villeneuve-Saint-Salves', 'Vincelles', 'Vincelottes'
]

# initialisation du dico pour stocker les résultats du comptage du populations
populations = {
    2008: {"immediate": 0, "totale": 0},
    2016: {"immediate": 0, "totale": 0},
    2021: {"immediate": 0, "totale": 0},
    2023: {"immediate": 0, "totale": 0}
}

# 2008
with open('donnees_2008.csv', newline="") as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    tete = []  # initialisation l'en-tête
    for ligne in csvfile:
        if csvfile.line_num == 1:  # lire la première ligne pour récupurer les noms des colonnes
            tete = ligne  # enregistrer la résultats
            col_commune = tete.index('Nom de la commune')
            col_population = tete.index('Population municipale')
        else:
            commune = ligne[col_commune]
            population = int(ligne[col_population])

            if commune in communes_immediate:
                populations[2008]['immediate'] += population
            if commune in communes_totale:
                populations[2008]['totale'] += population

# 2016
with open('donnees_2016.csv', newline="") as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    tete = []
    for ligne in csvfile:
        if csvfile.line_num == 1:
            tete = ligne
            col_commune = tete.index('Nom de la commune')
            col_population = tete.index('Population municipale')
        else:
            commune = ligne[col_commune]
            population = int(ligne[col_population])

            if commune in communes_immediate:
                populations[2016]['immediate'] += population
            if commune in communes_totale:
                populations[2016]['totale'] += population

# 2021
with open('donnees_2021.csv', newline="") as csvfile:
    csvfile = csv.reader(csvfile, delimiter=';')
    tete = []
    for ligne in csvfile:
        if csvfile.line_num == 1:
            tete = ligne
            col_commune = tete.index('COM')
            col_population = tete.index('PMUN')
        else:
            commune = ligne[col_commune]
            population = int(ligne[col_population])

            if commune in communes_immediate:
                populations[2021]['immediate'] += population
            if commune in communes_totale:
                populations[2021]['totale'] += population

# 2023
with open('donnees_2023.csv', newline="", encoding="utf-8") as csvfile:
    csvfile = csv.reader(csvfile, delimiter=';')
    tete = []
    for ligne in csvfile:
        if csvfile.line_num == 1:
            tete = ligne
            col_commune = tete.index('COM')
            col_population = tete.index('PMUN')
        else:
            commune = ligne[col_commune]
            population = int(ligne[col_population])

            if commune in communes_immediate:
                populations[2023]['immediate'] += population
            if commune in communes_totale:
                populations[2023]['totale'] += population

# visualisation des résultats
annees = list(populations.keys())
pop_immediate = [populations[annee]['immediate'] for annee in annees]
pop_totale = [populations[annee]['totale'] for annee in annees]

plt.plot(annees, pop_immediate, label='Population immédiate', marker='o')
plt.plot(annees, pop_totale, label='Population totale', marker='o')
plt.title('Évolution des populations (2008-2023)')
plt.xlabel('Année')
plt.ylabel('Population')
plt.legend()
plt.grid()
plt.show()
