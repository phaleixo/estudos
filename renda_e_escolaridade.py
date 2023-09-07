#Importando as Bibliotecas Necessárias

import pandas as pd
import numpy as np

#Extract

dados = pd.read_csv('dados_pessoas.csv')
media_sal = pd.read_csv('media_sal.csv')


#Transform

#Mesclar os dados das tabelas dados_pessoas.csv e media_sal.csv
tabela_final = dados.merge(media_sal,
                           left_on = 'ID',
                           right_on ='ID',
                           how='left' )
#Load
#Convertendo a tabela_final.csv para .xls e salvando
tabela_final.to_excel("sal_e_escolaridade.xlsx", index=False)


