import pandas
from matplotlib import pyplot as plt
import pyodbc
import numpy as np
from sqlalchemy import create_engine
import collections

conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\peter\PycharmProjects\pythonProject\veiculos.accdb;UID="";PWD="";')
cursor = conn.cursor()
# quantos foram produzidos



#######################QUERIES 2019 ##################################

cursor.execute("Select DTFAT from Veic where DTFAT >'190101' and DTFAT <'190131'")
jan = cursor.fetchall()
jan = len(jan)
cursor.execute("Select DTFAT from Veic where DTFAT >'190201' and DTFAT <'190231'")
fev = cursor.fetchall()
fev = len(fev)
cursor.execute("Select DTFAT from Veic where DTFAT >'190301' and DTFAT <'190331'")
mar = cursor.fetchall()
mar = len(mar)

cursor.execute("Select DTFAT from Veic where DTFAT >'190401' and DTFAT <'190431'")
abril = cursor.fetchall()
abril = len(abril)

cursor.execute("Select DTFAT from Veic where DTFAT >'190501' and DTFAT <'190531'")
maio = cursor.fetchall()
maio = len(maio)

cursor.execute("Select DTFAT from Veic where DTFAT >'190601' and DTFAT <'190631'")
junho = cursor.fetchall()
junho = len(junho)

cursor.execute("Select DTFAT from Veic where DTFAT >'190701' and DTFAT <'190731'")
julho = cursor.fetchall()
julho = len(julho)

cursor.execute("Select DTFAT from Veic where DTFAT >'190801' and DTFAT <'190831'")
agosto = cursor.fetchall()
agosto = len(agosto)

cursor.execute("Select DTFAT from Veic where DTFAT >'190901' and DTFAT <'190931'")
setem = cursor.fetchall()
setem = len(setem)

cursor.execute("Select DTFAT from Veic where DTFAT >'191001' and DTFAT <'191031'")
outu = cursor.fetchall()
outu = len(outu)

cursor.execute("Select DTFAT from Veic where DTFAT >'191101' and DTFAT <'191131'")
novem = cursor.fetchall()
novem = len(novem)


cursor.execute("Select DTFAT from Veic where DTFAT >'191201' and DTFAT <'191231'")
dezem = cursor.fetchall()
dezem = len(dezem)

#######################QUERIES 2019 ##################################

cursor.execute("Select DTFAT from Veic where DTFAT >'200101' and DTFAT <'200131'")
jan20 = cursor.fetchall()
jan20 = len(jan20)
cursor.execute("Select DTFAT from Veic where DTFAT >'200201' and DTFAT <'200231'")
fev20 = cursor.fetchall()
fev20 = len(fev20)
cursor.execute("Select DTFAT from Veic where DTFAT >'200301' and DTFAT <'200331'")
mar20 = cursor.fetchall()
mar20 = len(mar20)

cursor.execute("Select DTFAT from Veic where DTFAT >'200401' and DTFAT <'200431'")
abril20 = cursor.fetchall()
abril20 = len(abril20)

cursor.execute("Select DTFAT from Veic where DTFAT >'200501' and DTFAT <'200531'")
maio20= cursor.fetchall()
maio20 = len(maio20)
totalarrecadado = jan+fev+mar+abril+maio+junho+julho+agosto+setem+outu+novem+dezem+jan20+fev20+mar20+abril20+maio20

datafat = {'Meses': ['Janeiro/19','Fevereiro/19','Março/19','Abril/19','Maio/19','Junho/19','Julho/19','Agosto/19','Setembro/19','Outubro/19','Novembro/19','Dezembro19','Janeiro/20','Fevereiro/20','Março/20','Abril/20','Maio/20','Total faturado por mês'],
        'Vendas por mês': [jan,fev,mar,abril,maio,junho,julho,agosto,setem,outu,novem,dezem,jan20,fev20,mar20,abril20,maio20, totalarrecadado]
       }
df = pandas.DataFrame(datafat,columns=['Meses','Vendas por mês'])
df.plot(x ='Meses', y='Vendas por mês', kind = 'bar')

plt.show()