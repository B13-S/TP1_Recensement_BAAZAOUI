import csv

table2008=[]
donne2008=[]
table2016=[]
table2021=[]
table2023=[]
donneesFiltrer2008=[]
donneesFiltrer2016=[]
donneesFiltrer2021=[]
donneesFiltrer2023=[]
codeCommune=[]
CommuneVisser= ['Appoigny', 'Auxerre','Moneteau', 'Saint-Georges-sur-Baulche']
populationsTotale08=0
populationsTotale16=0
populationsTotale21=0
populationsTotale23=0

with open('donnees_2008.csv',newline="") as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        table2008.append(row)
        if row[6] in CommuneVisser:
            donneesFiltrer2008.append(row)
            populationsTotale08+=int(row[9])
        
with open('donnees_2016.csv',newline="") as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        table2016.append(row)
        if row[6] in CommuneVisser:
                donneesFiltrer2016.append(row)
                populationsTotale16+=int(row[9])




with open('donnees_2023.csv',newline="") as csvfile: 
    reader = csv.reader(csvfile,delimiter=';')
    for row in reader:
        table2023.append(row)
        if row[7] in CommuneVisser:
            donneesFiltrer2023.append(row)
            codeCommune.append(row)
            populationsTotale23+=int(row[10])


with open('donnees_2021.csv',newline="") as csvfile:
    reader = csv.reader(csvfile,delimiter=';')
    for row in reader:
        table2021.append(row)
        if row[2] in codeCommune:
          donneesFiltrer2021.append(row)
          populationsTotale21+=int(row[5])


print(codeCommune)
print("La populqtion de ",CommuneVisser ,"en 2008 est de :",populationsTotale08,"personnes")
print("La populqtion de ",CommuneVisser ,"en 2016 est de :",populationsTotale16,"personnes")
print("La populqtion de ",CommuneVisser ,"en 2021 est de :",populationsTotale21,"personnes")
print("La populqtion de ",CommuneVisser ,"en 2023 est de :",populationsTotale23,"personnes")
print(donneesFiltrer2008)
print(donneesFiltrer2016)
print(donneesFiltrer2021)
print(donneesFiltrer2023)




