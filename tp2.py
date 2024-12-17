import matplotlib.pyplot as plt
import csv

# déclarer des variables de comptage de résultat
total_hydraulique = 0
total_hydraulique_lacs = 0
total_hydraulique_step = 0
nombre_lignes_valides = 0

# je lus le fichier
with open('RTE_2022.csv', newline="") as fichier_csv:
    fichier_csv = csv.reader(fichier_csv, delimiter=',')
    en_tete = []
    for ligne in fichier_csv:
        if en_tete == []:  # lecture de l'en-tête
            en_tete = ligne
            # j'identifie les index des colonnes Hydraulique
            index_hydraulique = en_tete.index("Hydraulique")
            index_hydraulique_lacs = en_tete.index("Hydraulique - Lacs")
            index_hydraulique_step = en_tete.index("Hydraulique - STEP turbinage")
        else:
            ligne_vide = True
            for i in range(len(ligne)):
                if ligne[i].strip() != "":
                    ligne_vide = False
                    break
            ligne_non_vide = False
            for i in range(len(ligne)):
                if ligne[i].strip() != "":
                    ligne_non_vide = True
                    break
            if len(ligne) > 0 and ligne_non_vide:  # je prends en compte les colonnes et les lignes vide
                if len(ligne) > max(index_hydraulique, index_hydraulique_lacs, index_hydraulique_step):
                    # je récupère des valeurs des 3 colonnes Hydraulique
                    valeur_hydraulique = ligne[index_hydraulique].strip()
                    valeur_hydraulique_lacs = ligne[index_hydraulique_lacs].strip()
                    valeur_hydraulique_step = ligne[index_hydraulique_step].strip()

                    # Conversion et ajout si les valeurs sont valides
                    if valeur_hydraulique.replace('.', '').isdigit():
                        total_hydraulique += float(valeur_hydraulique)
                    if valeur_hydraulique_lacs.replace('.', '').isdigit():
                        total_hydraulique_lacs += float(valeur_hydraulique_lacs)
                    if valeur_hydraulique_step.replace('.', '').isdigit():
                        total_hydraulique_step += float(valeur_hydraulique_step)

                    nombre_lignes_valides += 1

print(f"Consommation totale Hydraulique : {total_hydraulique:.2f} GWh")
print(f"Consommation totale Hydraulique - Lacs : {total_hydraulique_lacs:.2f} GWh")
print(f"Consommation totale Hydraulique - STEP turbinage : {total_hydraulique_step:.2f} GWh")
print(f"Nombre de lignes valides : {nombre_lignes_valides}")


labels = ['Hydraulique', 'Hydraulique - Lacs', 'Hydraulique - STEP turbinage']
values = [total_hydraulique, total_hydraulique_lacs, total_hydraulique_step]
plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['blue', 'green', 'orange'])
plt.title('Répartition de la consommation hydraulique en 2022')
plt.ylabel('Consommation (GWh)')
plt.xlabel('Types de consommation hydraulique')
plt.show()