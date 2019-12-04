import pandas as pd
import matplotlib.pyplot as plt
#lendo a aba realizado, do arquivo dados
ler_realizado = pd.read_excel('dados.xlsx',sheet_name='realizado',
                        encoding='utf-8=sig',index_col=[0],skiprows=1)

#lendo a aba orcado, do arquivo dados
ler_orcado = pd.read_excel('dados.xlsx',sheet_name='orcado',index_col=[0]).T

#fazendo merge entre as abas
merge = pd.merge(ler_orcado,ler_realizado,how='outer')

#criado o arquivo de merge
merge_csv = pd.DataFrame.to_csv(merge,'merge.csv',index=False)

#lendo o arquivo de merge para transpor linhas e colunas
to_transport = pd.read_csv('merge.csv')
transported = to_transport.T

#matriz transposta do arquivo para ficar de acordo em relacao a linhas e colunas
transported_csv = transported.to_csv('merge_t.csv')

#lendo arquivo novo colocando o nome nas colunas
col_names = ['mes','orcado', 'realizado']
df = pd.read_csv('merge_t.csv',names=col_names,skiprows=1,encoding='utf-8=sig')

#criando a coluna diff
df['diff'] = 0

#alimentando dados da coluna diff
df['diff'] = df['orcado'] - df['realizado']

#gerar um resultado com todos os dados esperados
df.to_csv('result.csv',index=False)

#gerando as barras
plt.bar(df['mes'],df['orcado'], color = 'blue')
plt.bar(df['mes'], df['orcado']-df['diff'], color='orange',bottom=1)

#colocando a legenda nos eixos
plt.xlabel('mês')
plt.ylabel('$')

#colocando a box de legenda
plt.legend(('orçado','realizado'))

#colocando o titulo
plt.title("Gráfico Orçamento")

#plotando
plt.show()
