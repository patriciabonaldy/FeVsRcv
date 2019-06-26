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
urlFE = 'C:\\repositorio\\FeVsRcv\\datos\\redmine_52270_fe.txt'
urlRCV = 'C:\\repositorio\\FeVsRcv\\datos\\redmine_52270_rcv.txt'   
urlFinal = 'C:\\repositorio\\FeVsRcv\\datos\\redmine_52270_join.txt'         
    
df_FE = pd.read_csv(urlFE, delimiter=';')
df_RCV = pd.read_csv(urlRCV, delimiter=';')
print(df_FE.head(3))
print("------------------------")
print(df_RCV.head(3))
print("------------------------")
df_inner = pd.merge(df_FE, df_RCV, on='cuit_comprador', how='inner', suffixes=('_left','_right'))
print(df_inner.head(3))


           