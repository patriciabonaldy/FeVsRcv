"""
    @author: Patricia Bonaldy
    @created: 26/06/2019
    Join de 2 archivos por:
        'cuit','cuit_vendedor','fecha_emision_comprobante','tipo_cbte','nro_cbte_desde','nro_cbte_hasta','punto_de_venta'
        
    Si existe en FE, gana el importe_total de FE.
    Si no existe en FE, gana el importe_total de RCV.
    Si no existe en FE y no existe en RCV, lo excluis.    
"""
import numpy  as np
import pandas as pd
from IPython.display import display
from IPython.display import Image

#Importar la data
urlFE = 'C:\\Users\\dquintana\\pythonproect\\FeVsRcv\\datos\\redmine_52270_fe.txt'
urlRCV = 'C:\\Users\\dquintana\\pythonproect\\FeVsRcv\\datos\\redmine_52270_rcv.txt'   
urlFinal = 'C:\\Users\\dquintana\\pythonproect\\FeVsRcv\\datos\\redmine_52270_join.txt'         
    
df_FE = pd.read_csv(urlFE, delimiter=';')
df_RCV = pd.read_csv(urlRCV, delimiter=';')
#Hacemos merge por el PK
df_inner = pd.merge(df_FE, df_RCV, on=['cuit_comprador','cuit_vendedor','fecha_emision_comprobante','tipo_cbte','nro_cbte_desde','nro_cbte_hasta','punto_de_venta'], how='inner', suffixes=('_left','_right'))
df_inner = df_inner.dropna(subset=['importe_total_left','importe_total_right'])
#creamos una columna con el tipo de moneda y cae
df_inner = df_inner.assign(cae=df_inner['cae_left'])
df_inner = df_inner.assign(moneda=df_inner['moneda_right'])
#buscamos el universo que tiene importe left
df_Univ1= df_inner[df_inner['importe_total_left']>0]

#buscamos el universo que tiene importe right
df_Univ2= df_inner[df_inner['importe_total_left']<1]

#el conjunto que no tenga importe left le asignamos el right
df_Univ2 = df_Univ2.assign(importe_total_left=df_Univ2['importe_total_right'])

#unimos ambos universos
frames = [df_Univ1, df_Univ2]
df_inner = pd.concat(frames)


#creamos una columna con el importe final 
df_inner = df_inner.assign(importe_total=df_inner['importe_total_left'])
print(df_inner)
#borramos las columnas monedas e importe de ambos conjuntos
df_inner = df_inner.drop(['cae_left','cae_right','moneda_left', 'moneda_right','importe_total_left','importe_total_right'], axis=1)


#guardamos el contenido final
df_inner.to_csv(urlFinal)



           