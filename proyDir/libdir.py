# from distutils.cmd import Command
# from tkinter import INSERT, Tk, Label, Button
# from tkinter.tix import InputOnly

import re


nomenclaturas_urbanas=['','Carrera', 'carrera', 'CARRERA', 'KRA', 'kra', 'cra', 'CRA',  
    'calle', 'CALLE', 'Calle', 'CLL', 'cll' ,'CL','Cll','KR',
    'AL','Altillo','altillo','ALTILLO',
    'AU','Autopista','autopista','AUTOPISTA',
    'AVIAL','Anillo Vial','anillo vial','ANILLO VIAL','AnilloVial','anillovial','ANILLOVIAL','anillo Vial',
    'AC','Avenida Calle','avenida calle','AVENIDA CALLE','AvenidaCalle','avenidacalle','AVENIDACALLE',
    'AV','Avenida','avenida','AVENIDA',
    'AK','Avenida Carrera','avenida carrera','AVENIDA CARRERA','AvenidaCarrera','avenidacarrera','AVENIDACARRERA',
    'CRV','CV','cv','Circunvalar','circunvalar','CIRCUNVALAR',
    'CRT','Carretera','carretera','CARRETERA',
    'CT','Carretera','carretera','CARRETERA',
    'CV','Circunvalar','circunvalar','CIRCUNVALAR',
    'PQ','Parque','parque','PARQUE',
    'DP','Deposito','deposito','DEPOSITO','Depósito','depósito','DEPÓSITO',
    'EX','Exterior','exterior','EXTERIOR',
    'UR','Urbanización','urbanización','URBANIZACIÓN','Urbanizacion','urbanizacion','URBANIZACION',
    'VT','Variante','variante','VARIANTE',
    'VI','Vía','vía','VÍA','Via','via','VIA',
    'ZN','Zona','zona','ZONA',
    'CA','Casa','casa','CASA',
    'PAR','Parque','parque','PARQUE',
    'PJ','Pasaje','pasaje','PASAJE',
    'PL','Planta','planta','PLANTA',
    'TC','Troncal','troncal','TRONCAL',
    'PN','Puente','puente','PUENTE',
    'PRJ','Paraje','paraje','PARAJE',
    'SC','Salón Comunal','salón comunal','SALÓN COMUNAL','SalónComunal','salóncomunal','SALÓNCOMUNAL','Salon Comunal','salon comunal','SALON COMUNAL','SalonComunal','saloncomunal','SALONCOMUNAL',
    'SD','Salida','salida','SALIDA',
    'SL','Solar','solar','SOLAR',
    'GT','Glorieta','glorieta','GLORIETA',
    'VTE','VT','Variante','variante','VARIANTE',
    'PW','Park Way','park way','PARK WAY','ParkWay','parkway','PARKWAY','park Way','Park way',
    'CQ','Circular','circular','CIRCULAR',
    'TV','Transversal','transversal','TRANSVERSAL',
    'TC','Troncal','troncal','TRONCAL',
    'DG','Diagonal','diagonal','DIAGONAL',
    'PS','Paseo','paseo','PASEO',
    'PT','Peatonal','peatonal','PEATONAL',
    'Boulevard', 'boulevard', 'BOULEVARD', 'bulevard', 'Bulevard', 'BULEVARD', 'bulevar', 'Bulevar',
    'BULEVAR', 'BL', 'bl',
    'Cuentas Corridas', 'cuentas corridas','CUENTAS CORRIDAS', 'CuentasCorridas', 'cuentascorridas', 'Cc',
    'CUENTASCORRIDAS', 'cuentas Corridas', 'cuentas Corridas', 'cuentasCorridas', 'cuentasCorridas', 'CC', 'cc',    
    'cv','dp','et','fi','km','cv',
    'lt','mz','pq','pl','pd','sc','ur','vt','vi','zn',
    'ca','sc','sd','sec','sl','terpln','vte','pw','cq',
    'tc','dg','cc','Tc','tc','vt']


nomenclaturas_rurales=['','AL','Altillo','altillo','ALTILLO',
    'APTDO','Apartado','apartado','ALTILLO',
    'AVIAL','Anillo Vial','anillo vial','ANILLO VIAL','AnilloVial','anillovial','ANILLOVIAL','anillo Vial'
    'C','Corregimiento','corregimiento','CORREGIMIENTO',
    'CA','Casa','casa','CASA',
    'CAS','Caserío','caserío','CASERÍO','Caserio','caserio','CASERIO',
    'CD','Ciudadela','ciudadela','CIUDADELA',
    'CN','Camino','camino','CAMINO',
    'CRT','Carretera','carretera','CARRETERA','CT',
    'CRV','Circunvalar','circunvalar','CIRCUNVALAR',
    'DP','Deposito','deposito','DEPOSITO','Depósito','depósito','DEPÓSITO'
    'EX','Exterior','exterior','EXTERIOR',
    'FCA','Finca','finca','FINCA',
    'GT','Glorieta','glorieta','GLORIETA',
    'DPTO','Departamento','departamento','DEPARTAMENTO',
    'HC','Hacienda','hacienda','HACIENDA',
    'HG','Hangar','hangar','HANGAR',
    'KM','Kilómetro','kilómetro','KILÓMETRO','Kilometro','kilometro','KILOMETRO',
    'LT','Lote','lote','LOTE',
    'MLL','Muelle','muelle','MUELLE',
    'PA','Parcela','parcela','PARCELA',
    'PAR','Parque','parque','PARQUE',
    'PL','Planta','planta','PLANTA',
    'PD','Predio','predio','PREDIO',
    'PN','Puente','puente','PUENTE',
    'PRJ','Paraje','paraje','PARAJE',
    'SC','Salón Comunal','salón comunal','SALÓN COMUNAL','SalónComunal','salóncomunal','SALÓNCOMUNAL','Salon Comunal','salon comunal','SALON COMUNAL','SalonComunal','saloncomunal','SALONCOMUNAL',
    'SD','Salida','salida','SALIDA',
    'SEC','Sector','sector','SECTOR',
    'SL','Solar','solar','SOLAR',
    'TERPLN','Terraplén','terraplén','TERRAPLÉN','Terraplen','terraplen','TERRAPLEN',
    'VTE','Variante','variante','VARIANTE',
    'TV','Transversal','transversal','TRANSVERSAL',
    'VDA','Vereda','vereda','VEREDA',
    'VT','Variante','variante','VARIANTE',
    'ZF','Zona Franca','zona franca','ZONA FRANCA','ZonaFranca','zonafranca','ZONAFRANCA','Zona franca','zona Franca','Zonafranca','zonaFranca',
    'ZN','Zona','zona','ZONA',
    'PS','Paseo','paseo','PASEO',
    'PT','Puesto','puesto','PUESTO',
    'VT','Variante','variante','VARIANTE',
    'VI','Vía','vía','VÍA','Via','via','VIA',
    'Vereda','vereda','VEREDA','VDA','vda','vd','VD'
    'TC','Troncal','troncal','TRONCAL',
    'al', 'aptdo','avial','c','ca','cas','cd',
    'cn','crt','crv','dpto','dp','dp','ex','fca','gt','hc',
    'hg','km','lt','mll','pa','par','pl','pd','pn','prj',
    'sc','sd','sec','sl','terpln','tv','vda','vt','vte','zf',
    'zn','ps','pt','pw','via','vi','tc']

orientacion=['','Este', 'Norte', 'Oeste', 'Sur',
    'este', 'norte', 'oeste', 'sur'
    'ESTE', 'NORTE', 'OESTE', 'SUR']

simbolo=['#','N','N°','No','N0','numero',
    'Numero','número','Número','NUMERO']

bis=['BIS','Bis','bis']

complementos=['','ad','administración','AD','ADMINISTRACIÓN','Ad','Administración',
    'ag','AG','AGRUPACIÓN','Ag','Agrupación','agrupación','AGRUPACION','Agrupacion','agrupacion',
    'AL','Altillo','altillo','ALTILLO','al','Al',
    'ap','apartamento','AP','APARTAMENTO','Ap','Apartamento',
    'br','barrio','BR','BARRIO','Br','Barrio',
    'bq','bloque','BQ','BLOQUE','Bq','Bloque',
    'bg','bodega','BG','BODEGA','Bg','Bodega',
    'CA','Casa','casa','CASA','Ca','ca',
    'cu','célula','CU','CÉLULA','Cu','Célula','celula','CU','CELULA','Cu','Celula',
    'ce','centro comercial','CE','CENTRO COMERCIAL','Ce','Centro Comercial','centrocomercial','CENTROCOMERCIAL','CentroComercial',
    'co','conjunto residencial','CO','CONJUNTO RESIDENCIAL','Co','Conjunto Residencial','conjuntoresidencial','CONJUNTORESIDENCIAL','ConjuntoResidencial',
    'cn','consultorio','CN','CONSULTORIO','Cn','Consultorio',
    'CD','Ciudadela','ciudadela','CIUDADELA','cd','Cd','DPTO','Departamento','departamento','DEPARTAMENTO',
    'DPTO','Departamento','departamento','DEPARTAMENTO',
    'DP','Deposito','deposito','DEPOSITO','Depósito','depósito','DEPÓSITO',
    'ds','depósito sótano','DS','DEPÓSITO SÓTANO','Ds','Deposito Sótano','deposito sotano','DEPOSITO SOTANO','Deposito Sotano',
    'ed','edificio','ED','EDIFICIO','Ed','Edificio',
    'en','entrada','EN','ENTRADA','En','Entrada',
    'eq','esquina','EQ','ESQUINA','Eq','Esquina',
    'es','estación','ES','ESTACIÓN','Es','Estación',
    'et','etapa','ET','ETAPA','Et','Etapa',
    'EX','Exterior','exterior','EXTERIOR',
    'FCA','Finca','finca','FINCA','FI','fi','Fi','fca',
    'ga','garaje','GA','GARAJE','Ga','Garaje',
    'gs','garaje sótano','GS','GARAJE SÓTANO','Gs','Garaje Sótano','garaje sotano','GARAJE SOTANO','Garaje Sotano',
    'in','interior','IN','INTERIOR','In','Interior',
    'KM','Kilómetro','kilómetro','KILÓMETRO','Kilometro','kilometro','KILOMETRO',
    'lc','local','LC','LOCAL','Lc','Local',
    'lm','local mezzanine','Lm','Local Mezzanine','LM','LOCAL MEZZANINE',
    'LT','Lote','lote','LOTE',
    'mz','manzana','MZ','MANZANA','Mz','Manzana',
    'mn','mezzanine','MN','MEZZANINE','Mn','Mezzanine',
    'md','módulo','MD','MÓDULO','Md','Módulo','modulo','MODULO','Modulo',
    'of','oficina','OF','OFICINA','Of','Oficina',
    'PAR','Parque','parque','PARQUE','Pq','pq',
    'pa','parqueadero','PA','PARQUEADERO','Pa','Parqueadero',
    'pn','penthouse','PN','PENTHOUSE','Pn','Penthouse',
    'pi','piso','PI','PISO','Pi','Piso',
    'pl','planta','Pl','Planta','PL','PLANTA',
    'pr','porteria','Pr','Porteria','PR','PORTERIA',
    'PD','Predio','predio','PREDIO','pd','Pd',
    'pu','puesto','Pu','Puesto ','PU','PUESTO',
    'rp','round point','RP','ROUND POINT','Rp','Round Point',
    'SEC','Sector','sector','SECTOR','SC','sc','Sc',
    'ss','semisótano','SS','SEMISÓTANO','Ss','Semisótano','semisotano','SEMISOTANO','Semisotano',
    'so','sótano','SO','SÓTANO','So','Sótano','sotano','SOTANO','Sotano',
    'st','suite','ST','SUITE','St','Suite',
    'sm','supermanzana','SM','SUPERMANZANA','Sm','Supermanzana',
    'tz','terraza','TZ','TERRAZA','Tz','Terraza',
    'to','torre','TO','TORRE','To','Torre',
    'un','unidad','UN','UNIDAD','Un','Unidad',
    'ul','unidad residencial','UL','UNIDAD RESIDENCIAL','Ul','Unidad Residencial',
    'ur','urbanización','UR','URBANIZACIÓN','Ur','Urbanización','urbanizacion','URBANIZACION','Urbanizacion',
    'ZN','Zona','zona','ZONA','zn'
]



tipo_predio=['AL','Altillo','altillo','ALTILLO','al','Al',
    'ap','apartamento','AP','APARTAMENTO','Ap','Apartamento',
    'bg','bodega','BG','BODEGA','Bg','Bodega',
    'CA','Casa','casa','CASA','Ca','ca',
    'cn','consultorio','CN','CONSULTORIO','Cn','Consultorio',
    'DP','Deposito','deposito','DEPOSITO','Depósito','depósito','DEPÓSITO',
    'ds','depósito sótano','DS','DEPÓSITO SÓTANO','Ds','Depósito Sótano','deposito sotano','DEPOSITO SOTANO','Deposito Sotano',
    'ga','garaje','GA','GARAJE','Ga','Garaje',
    'gs','garaje sótano','GS','GARAJE SÓTANO','Gs','Garaje Sótano','garaje sotano','GARAJE SOTANO','Garaje Sotano',
    'lc','local','LC','LOCAL','Lc','Local',
    'lm','local mezzanine','Lm','Local Mezzanine','LM','LOCAL MEZZANINE',
    'LT','Lote','lote','LOTE',
    'mn','mezzanine','MN','MEZZANINE','Mn','Mezzanine',
    'of','oficina','OF','OFICINA','Of','Oficina',
    'pa','parqueadero','PA','PARQUEADERO','Pa','Parqueadero',
    'pn','penthouse','PN','PENTHOUSE','Pn','Penthouse',
    'pl','planta','Pl','Planta','PL','PLANTA',
    'PD','Predio','predio','PREDIO','pd','Pd',
    'ss','semisótano','SS','SEMISÓTANO','Ss','Semisótano','semisotano','SEMISOTANO','Semisotano',
    'so','sótano','SO','SÓTANO','So','Sótano','sotano','SOTANO','Sotano',
    'st','suite','ST','SUITE','St','Suite',
    'tz','terraza','TZ','TERRAZA','Tz','Terraza',
    'un','unidad','UN','UNIDAD','Un','Unidad',
    'ul','unidad residencial','UL','UNIDAD RESIDENCIAL','Ul','Unidad Residencial'
]

urbanizacion=[
    'bq','bloque','BQ','BLOQUE','Bq','Bloque',
    'cu','célula','CU','CÉLULA','Cu','Célula',
    'co','conjunto residencial','CO','CONJUNTO RESIDENCIAL','Co','Conjunto Residencial','conjuntoresidencial','CONJUNTORESIDENCIAL','ConjuntoResidencial',
    'et','etapa','ET','ETAPA','Et','Etapa',
    'ur','urbanización','UR','URBANIZACIÓN','Ur','Urbanización'
    'SEC','Sector','sector','SECTOR','SC','sc','Sc',
    'to','torre','TO','TORRE','To','Torre',
    'ZN','Zona','zona','ZONA','zn'
]
barrio=['br','barrio','BR','BARRIO','Br','Barrio',
    'CD','Ciudadela','ciudadela','CIUDADELA','cd','Cd',
    'sm','supermanzana','SM','SUPERMANZANA','Sm','Supermanzana'
]


patron1=re.compile(r"((^[a-zA-Z]+)\s?(\d{1,3})?\s?([a-zA-Z]*)\s?(\.\-\d)?([n#\-\°]*)(.*)(\d{1,3})+([a-zA-Z]*)\s?(\-)*\s?(\d{1,3})*\s?(\w\s?)*)", re.I )
patron2=re.compile(r"((^[a-zA-Z]+)\s?(\d{1,3})?\s?([a-zA-Z]*)\s?(\.\-)?([bis]?)\s?([a-zA-Z]*)\s?([nº#\-\°\.]*)\s?(\d{1,3})+([a-zA-Z]*)\s?(\-)*\s?(\d{1,3})*\s?(\w\s?)*([\w,\w,\w]*))", re.I )
#patron3 = re.compile(r"((Calle|Carrera|Transversal|Diagonal)+([ ][0-9]|[ ][0-9]\d)+(([ ][ABCD])*)+(([ ]Norte|[ ]Sur)*)+([ ][#])+([ ][0-9]|[ ][0-9]\d)+(([ ][ABCD])*)+([ ][0-9]|[ ][0-9]\d))$|(Km)+(([ ]via)*)+([ ][0-9]|[ ][0-9]\d)+([ ][a-z]*)*$")



patronprim=re.compile(r'^([a-zA-Z]+)\s?\d{1,3}\s?(\.\-)?\s?(\d{1,3})*\s?[a-zA-Z]+(\W)*\s?([bis]{1,3})*[a-zA-Z]*\s?(este|oeste|sur|norte)*',re.I)
patronsimbolos=re.compile(r'\s?([m-n])*(\.?\s?)(#|°|º|um|umero|úm|úmero?)',re.I)
placa =re.compile(r'\s?(\d{1,3})*\s?([bis]{1,3})*([a-zA-Z]*)\s?\-+(\d{1,3})*\s?(este|oeste|sur|norte)*',re.I)
complem =re.compile(r'\s([a-zA-Z]+)\s?([a-zA-Z]*)\s?([a-zA-Z]*)\s?(\d{1,3})*\s?\,?(\s?\w*\s?\w*)\,?\w*\s?',re.I)
rurales=re.compile(r'^([a-zA-Z]+)\s?(([\w]+)\s?){1,10}(\,?\s?([\w]+)\s?){1,10}',re.I)
#expresion1=patronprim,patronsimbolos,placa

prueba=("Calle 32D sur n.º 6-32 este")
rur=("Vereda San Antonio finca tal , municipio tuta")
expini=re.search(patronprim,prueba)
# print(ex1)
# print(f'{ex1.group(1)}')
expcom=re.search(complem,prueba)
expcomru=re.match(rurales,rur)
print(expcomru)
print(f'{expcomru.group(1)}')
# # print(v)
# # print(f'{v.group(0)}')
expplac=re.search(placa,prueba)
# print(v)
# print(f'{v.group(0)}')
expsim=re.search(patronsimbolos,prueba)
# print(num)
# print(f'{num.group(0)}')
# for line in nomenclaturas_urbanas:
#     if v.group(0)==line:
#         print(line)
#         print(f'{v.group(0)}')

def valida1(entrada):
    for line in nomenclaturas_urbanas:
        expini=re.search(patronprim,entrada)
        expsim=re.search(patronsimbolos,entrada)
        expplac=re.search(placa,entrada)
        expcom=re.search(complem,entrada)
        if expini.group(1)==line:
            if expsim and expplac:
                print(f'{expini.group(0)}{expsim.group(0)}{expplac.group(0)}')
                return  print("Expresión valida y urbana")
            else:
                return  print("Expresión no valida")

def valida2(entrada):
    for line in nomenclaturas_rurales:
        expcomru=re.match(rurales,entrada)
        if expcomru.group(1)==line:
            return  print("Expresión valida y rural")
                     

# def valida2():
#     for line in nomenclaturas_rurales:
#         if expcom.group(1)==line:
#             print(expcom)
#             print(f'{expcom.group(0)}')
#             return print(f'{expcom.group(0)}')

#Calle 111 No. 100 - 11� Barrio el Estadio;CRA 81 A 81 20 CASA DE LA CULTURA ; Calle 150 No. 9 - 56 centro; CALLE 93 N° 96A- 09
#Carrera 10A No. 20 - 40� Edificio El Clar�n piso 3 Centro La Matuna;CARRERA 50 N� 52-52
#profe
#Calle 32D sur n.º 6-32 este         Carrera 16-4 # 36-38
#Diagonal 43B. BisA Sur núm 6C-32 Blq F int 4
#Vereda San Antonio finca tal municipio tuta
#no valida  #Transv 3 bis Norte B # 7-11A Barrio la perseverancia, Bogotá D.C, Colombia
#Vereda el altillo lote 43             Diagonal 43 Bis Norte # 18-14 Manzana B
# Mz 3 bis  # 7A-11 , C.C Universal, Bogotá D.C, Colombia
#  Transv 3^ra bis Norte b # 7A-11 barrio La perseverancia, Bogotá D.C, Colombia
#Circunvalar y edificio
#Rural con predio
#Ciudadela bloque apartamento interior
# Sin edificio no es válido Oficina
#Unidad residencia          Esquina
#Carretera central del norte km 20 vía toca
#Parque industruak
#print(valida1("Calle 32D sur n.º 6-32 este"))
print(valida2("Vereda San Antonio finca tal , municipio tuta"))
#print(valida1("Carrera 16-4 # 36-38"))
# print(valida1("Diagonal 43B. BisA Sur núm 6C-32 Blq F int 4"))
# print(valida1("Mz 3 bis  # 7A-11 , C.C Universal, Bogotá D.C, Colombia"))



















# class VentanaEjemplo:
#     def __init__(self, master):
#         self.master = master
#         master.title("Direcciones validas en Colombia")

#         self.etiqueta = Label(master, text="Ingresa la dirección que deseas evaluar:")
#         self.etiqueta.pack()

#         #self.inputt=InputOnly(master,text="Ingresa aquí",Command=self.inputt)
#         #self.inputt.pack()

#         self.botonSaludo = Button(master, text="Comprobar", command=self.saludar)
#         self.botonSaludo.pack()

#         self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
#         self.botonCerrar.pack()

#     def saludar(self):
#         print("¡Hey!")
    
#     def input(self):
#         print(self.inputt)


# root = Tk()
# miVentana = VentanaEjemplo(root)
# root.mainloop()