import pandas
from matplotlib import pyplot as plt
import pyodbc

#  ------------------------------ CONNECTION STARTER ------------------------------
conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\peter\PycharmProjects\pythonProject\veiculos.accdb;UID="";PWD="";')
cursor = conn.cursor()

#  ------------------------------ DESAFIO 01 ------------------------------
cursor.execute("Select CodPais from Veic where CodPais = 'BRA' and DTFLI < '200000' and DTFLI >'190000'")
data = cursor.fetchall()  # Brasil
cursor.execute("Select CodPais from Veic where CodPais = '901' and DTFLI < '200000' and DTFLI >'190000'")
data1 = cursor.fetchall()  # australia
cursor.execute("Select CodPais from Veic where CodPais = '601' and DTFLI < '200000' and DTFLI >'190000'")
data2 = cursor.fetchall()  # EGITO
cursor.execute("Select CodPais from Veic where CodPais = '605' and DTFLI < '200000' and DTFLI >'190000'")
data3 = cursor.fetchall()  # ETIOPIA
cursor.execute("Select CodPais from Veic where CodPais = '643' and DTFLI < '200000' and DTFLI >'190000'")
data4 = cursor.fetchall()  # NIGERIA
cursor.execute("Select CodPais from Veic where CodPais = '675' and DTFLI < '200000' and DTFLI >'190000'")
data5 = cursor.fetchall()  # AFRICADOSUL
cursor.execute("Select CodPais from Veic where CodPais = '723' and DTFLI < '200000' and DTFLI >'190000'")
data6 = cursor.fetchall()  # COSTARICA
cursor.execute("Select CodPais from Veic where CodPais = '725' and DTFLI < '200000' and DTFLI >'190000'")
data7 = cursor.fetchall()  # REP.DOMINICANA
cursor.execute("Select CodPais from Veic where CodPais = '727' and DTFLI < '200000' and DTFLI >'190000'")
data8 = cursor.fetchall()  # GUATEMALA
cursor.execute("Select CodPais from Veic where CodPais = '729' and DTFLI < '200000' and DTFLI >'190000'")
data9 = cursor.fetchall()  # HAITI
cursor.execute("Select CodPais from Veic where CodPais = '737' and DTFLI < '200000' and DTFLI >'190000'")
data10 = cursor.fetchall()  # MEXICO
cursor.execute("Select CodPais from Veic where CodPais = '739' and DTFLI < '200000' and DTFLI >'190000'")
data11 = cursor.fetchall()  # NICARAGUA
cursor.execute("Select CodPais from Veic where CodPais = '741' and DTFLI < '200000' and DTFLI >'190000'")
data12 = cursor.fetchall()  # PANAMA
cursor.execute("Select CodPais from Veic where CodPais = '751' and DTFLI < '200000' and DTFLI >'190000'")
data13 = cursor.fetchall()  # BARBADOS
cursor.execute("Select CodPais from Veic where CodPais = '771' and DTFLI < '200000' and DTFLI >'190000'")
data14 = cursor.fetchall()  # ARGENTINA
cursor.execute("Select CodPais from Veic where CodPais = '773' and DTFLI < '200000' and DTFLI >'190000'")
data15 = cursor.fetchall()  # BOLIVIA
cursor.execute("Select CodPais from Veic where CodPais = '777' and DTFLI < '200000' and DTFLI >'190000'")
data16 = cursor.fetchall()  # CHILE
cursor.execute("Select CodPais from Veic where CodPais = '779' and DTFLI < '200000' and DTFLI >'190000'")
data17 = cursor.fetchall()  # EQUADOR
cursor.execute("Select CodPais from Veic where CodPais = '785' and DTFLI < '200000' and DTFLI >'190000'")
data18 = cursor.fetchall()  # COLOMBIA
cursor.execute("Select CodPais from Veic where CodPais = '787' and DTFLI < '200000' and DTFLI >'190000'")
data19 = cursor.fetchall()  # PARAGUAI
cursor.execute("Select CodPais from Veic where CodPais = '789' and DTFLI < '200000' and DTFLI >'190000'")
data20 = cursor.fetchall()  # PERU
cursor.execute("Select CodPais from Veic where CodPais = '793' and DTFLI < '200000' and DTFLI >'190000'")
data21 = cursor.fetchall()  # URUGUAI
cursor.execute("Select CodPais from Veic where CodPais = '843' and DTFLI < '200000' and DTFLI >'190000'")
data22 = cursor.fetchall()  # JORDANIA
cursor.execute("Select CodPais from Veic where CodPais = '869' and DTFLI < '200000' and DTFLI >'190000'")
data23 = cursor.fetchall()  # FILIPINAS
cursor.execute("Select CodPais from Veic where CodPais = '882' and DTFLI < '200000' and DTFLI >'190000'")
data24 = cursor.fetchall()  # VIETNADONORTE

brasil = (len(data))
australia = (len(data1))
egito = (len(data2))
etiopia = (len(data3))
NIGERIA = (len(data4))
COSTARICA = (len(data6))
REP_DOMINICANA = (len(data7))
GUATEMALA = (len(data8))
HAITI = (len(data9))
MEXICO = (len(data10))
NICARAGUA = (len(data11))
PANAMA = (len(data12))
BARBADOS = (len(data13))
ARGENTINA = (len(data14))
BOLIVIA = (len(data15))
CHILE = (len(data16))
EQUADOR = (len(data17))
COLOMBIA = (len(data18))
PARAGUAI = (len(data19))
PERU = (len(data20))
URUGUAI = (len(data21))
JORDANIA = (len(data22))
FILIPINAS = (len(data23))
VIETNADONORTE = (len(data23))


#  ------------------------------ GRAPH MAKER ------------------------------

dataend = {'Country': ['Brasil', 'australia', 'egito', 'etiopia', 'NIGERIA', 'COSTARICA', 'REP_DOMINICANA', 'GUATEMALA',
                       'HAITI', 'MEXICO', 'NICARAGUA', 'PANAMA', 'BARBADOS', 'ARGENTINA', 'BOLIVIA', 'CHILE', 'EQUADOR',
                       'COLOMBIA', 'PARAGUAI', 'PERU', 'URUGUAI', 'JORDANIA', 'FILIPINAS', 'VIETNADONORTE'],
           'Carros Vendidos': [brasil, australia, egito, etiopia, NIGERIA, COSTARICA, REP_DOMINICANA, GUATEMALA, HAITI,
                               MEXICO, NICARAGUA, PANAMA, BARBADOS, ARGENTINA, BOLIVIA, CHILE, EQUADOR, COLOMBIA,
                               PARAGUAI, PERU, URUGUAI, JORDANIA, FILIPINAS, VIETNADONORTE]
           }

df = pandas.DataFrame(dataend, columns=['Country', 'Carros Vendidos'])
df.plot(x='Country', y='Carros Vendidos', kind='bar')
plt.show()
#  ------------------------------ DESAFIO 02 ------------------------------

# quantos foram produzidos
cursor.execute("Select DTFLI from Veic where DTFLI >'1'")
result = cursor.fetchall()

# quantos foram liberados
cursor.execute("Select DTLCO_1a from Veic where DTLCO_1a >'1'")
liberados = cursor.fetchall()

totalproduzidos = (len(result))
print(totalproduzidos)

TOTALliberados = (len(liberados))
print(TOTALliberados)

x = 100 * TOTALliberados / totalproduzidos
porcentovendidos = ('%.2f' % x)

datavis = [porcentovendidos, 27.16]
label = ['Efetivamente Liberados', 'Não liberados']

# DATAVIS
plt.pie(datavis, labels=label, autopct='%1.1f%%', explode=[0, 0], shadow=True, startangle=90)
plt.title('Total de carros produzidos')
plt.axis('equal')

plt.show()
#  ------------------------------ DESAFIO 03 ------------------------------

#  ------------------------------ QUERIES 2019 ------------------------------


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

#  ------------------------------ QUERIES 2020 ------------------------------

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
maio20 = cursor.fetchall()
maio20 = len(maio20)
totalarrecadado = jan + fev + mar + abril + maio + junho + julho + agosto + setem + outu + novem + dezem + jan20 + fev20 + mar20 + abril20 + maio20

datafat = {
    'Meses': ['Janeiro/19', 'Fevereiro/19', 'Março/19', 'Abril/19', 'Maio/19', 'Junho/19', 'Julho/19', 'Agosto/19',
              'Setembro/19', 'Outubro/19', 'Novembro/19', 'Dezembro19', 'Janeiro/20', 'Fevereiro/20', 'Março/20',
              'Abril/20', 'Maio/20'],
    'Faturados por mês': [jan, fev, mar, abril, maio, junho, julho, agosto, setem, outu, novem, dezem, jan20, fev20, mar20,
                       abril20, maio20]
    }
df = pandas.DataFrame(datafat, columns=['Meses', 'Faturados por mês'])
df.plot(x='Meses', y='Faturados por mês', kind='bar')

plt.title("O total de carros faturados é de {}".format(totalarrecadado))

plt.show()
