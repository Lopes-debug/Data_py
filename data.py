# from tqdm import tqdm    #exibir barra de carregamento ao executar código
# import requests          #tratar arquivos csv da internet
# import io                #tratar arquivos csv da internet
from openpyxl import Workbook, load_workbook
import pandas as pd
import matplotlib.pyplot as plt

# vendas_df = pd.read_csv(r"C:\Users\leand\Downloads\Python_Impressionador-001\#Cursos\Hashtag\Python Impressionador\19.Análise da Dados com o Pandas + Integração Python e Excel\MATERIAL DE APOIO\Contoso - Vendas  - 2017.csv", sep=';')

# clientes_df = pd.read_csv(r"C:\Users\leand\Downloads\Python_Impressionador-001\#Cursos\Hashtag\Python Impressionador\19.Análise da Dados com o Pandas + Integração Python e Excel\MATERIAL DE APOIO\clientes.csv", sep=';')

# lojas_df = pd.read_csv(r"C:\Users\leand\Downloads\Python_Impressionador-001\#Cursos\Hashtag\Python Impressionador\19.Análise da Dados com o Pandas + Integração Python e Excel\MATERIAL DE APOIO\Contoso - Lojas.csv", sep=';', encoding='utf-8')

# produtos_df = pd.read_csv(r"C:\Users\leand\Downloads\Python_Impressionador-001\#Cursos\Hashtag\Python Impressionador\19.Análise da Dados com o Pandas + Integração Python e Excel\MATERIAL DE APOIO\Novo Vendas Produtos.csv", encoding='latin-1')

# vendas_format = vendas_df[['ID Loja', 'Data da Venda', 'Quantidade Vendida', 'Quantidade Devolvida']]
# clientes_format = clientes_df[['ID Cliente', 'Primeiro Nome','Sobrenome','E-mail']]
# lojas_format = lojas_df[['ID Loja','Nome da Loja', 'País']]
# lojas_format = lojas_format.rename(columns={'ID Loja':'ID Cliente'})
# clientes_format = clientes_format.merge(lojas_format, on='ID Cliente')
# print(clientes_format)

#Contar quantas vezes aparece o mesmo nome na coluna e exibir num gráfico 
# hertz = clientes_format['E-mail'].value_counts()
# view = hertz[:4].plot(figsize=(10,5))
# plt.show()

#Agrupar nomes repetidos e somar o total das vendas
# vendas_format = vendas_format.groupby('ID Loja').sum()
# vendas_format = vendas_format.sort_values('Quantidade Vendida', ascending=False)
# vendas_format[:4].plot(figsize=(10,5), kind = 'bar')
# plt.show()

#Ordenar a lista decrescente, pegar o maior valor e seu indice
# maior_valor = vendas_format['Quantidade Vendida'].max()
# index_maior_valor = vendas_format['Quantidade Vendida'].idxmax()

#Pegar o menor valor e seu índice
# print(vendas_format[-1:])
# ou usando .min() e .idxmin()

# aplicar uma "condição"
# idloja = vendas_format[vendas_format['ID Loja'] == 300]
# sum = idloja['Quantidade Vendida'].sum()
# mus = idloja['Quantidade Devolvida'].sum()
# print('{:.2%}'.format(mus/sum))
# print(idloja)


# EXERCICIO 1 - Aplicando "condições" para filtrar uma coluna (linhas acima também ^)

# primeira forma(separado):
# idloja = vendas_format['ID Loja'] == 305
# devol = vendas_format['Quantidade Devolvida'] == 0
# final = vendas_format[idloja & devol]
# print(final)

# segunda forma(junto):
# alljunto = vendas_format[(vendas_format['ID Loja'] == 305) & (vendas_format['Quantidade Devolvida'] == 0)]
# print(alljunto)

# modificar formato da data
# vendas_format['Data da Venda'] = pd.to_datetime(vendas_format['Data da Venda'], format='%d/%m/%Y')

# adicionar novas colunas no dataFrame
# vendas_format['Ano da Venda'] = vendas_format['Data da Venda'].dt.year
# vendas_format['Mês da Venda'] = vendas_format['Data da Venda'].dt.month
# vendas_format['Dia da Venda'] = vendas_format['Data da Venda'].dt.day

# alterando índice do dataframe, que passará a ser o nome da loja
# print(produtos_df.head())
# produtos_df = produtos_df.set_index('produtos')

# acessando informação com o novo índice 'produtos' usando .loc
# print(produtos_df.loc['webcam', 'Vendas 2019'])

# primeira forma para alterar o valor usando o novo índice
# produtos_df.loc['webcam', 'Vendas 2019'] = 1700

# acessando informação através da linha, coluna usando iloc. 
# print(produtos_df.iloc[12, 0])

# segunda forma para alterar o valor usando índice antigo
# vendas_format.loc[vendas_format['ID Loja'] == 294, 'Quantidade Devolvida'] = 1700

# criando um csv
# lojas_format.to_csv(r'Testando Brainless.csv', sep=';')

# criando DataFrame a partir de um dicionário
# vendas_produtos = {'iphone': [558147, 951642], 'galaxy': [712350, 244295], 'ipad': [573823, 26964], 'tv': [405252, 787604], 'máquina de café': [718654, 867660], 'kindle': [531580, 78830], 'geladeira': [973139, 710331], 'adega': [892292, 646016], 'notebook dell': [422760, 694913], 'notebook hp': [154753, 539704], 'notebook asus': [887061, 324831], 'microsoft surface': [438508, 667179], 'webcam': [237467, 295633], 'caixa de som': [489705, 725316], 'microfone': [328311, 644622], 'câmera canon': [591120, 994303]}

# vendas_produtos_df = pd.DataFrame.from_dict(vendas_produtos, orient='index')
# vendas_produtos_df = vendas_produtos_df.rename(columns={0: 'Vendas 2010', 1: 'Vendas 2011'})
# vendas_produtos_df = vendas_produtos_df['Vendas 2010']
# vendas_produtos_df.to_csv(r'DicioCSV.csv', sep= ';', encoding='latin1')
# print(vendas_produtos_df)

# tratamento de link csv que não abre facilmente
# url = 'http://www.transparencia.go.gov.br/portaldatransparencia/institucional/dados-abertos'
# conteudo_url = requests.get(url).content
# arquivo = io.StringIO(conteudo_url.decode('latin1'))
# cafe_df = pd.read_csv(arquivo, sep=',')
# print(cafe_df)


# Excel - Pandas x Openpyxl
# Pandas (facil modificar porém lê apenas como dados, excluindo gráficos e fórmulas ao editar)
# Openpyxl (mais trabalhoso modificar porém mantém os gráficos e fórmulas originais)


# Pandas

# pandas_format = pd.read_excel("Produtos.xlsx")
# pandas_format.loc[pandas_format['Tipo']=='Serviço', 'Multiplicador Imposto'] = 1.5
# pandas_format['Preço Base Reais'] = pandas_format['Multiplicador Imposto'] * pandas_format['Preço Base Original']
# pandas_format.to_excel(r'ModoPanda.xlsx')


# Openpyxl

# planilha = load_workbook("Produtos.xlsx")
# aba_ativa = planilha.active

# for celula in aba_ativa["C"]:
#     if celula.value == "Serviço":
#         linha = celula.row
#         aba_ativa[f"D{linha}"] = 1.5
        
# planilha.save("ProdutosOpenPy.xlsx")


# Implementar barra de carregamento de execução do código
# from tqdm import tqdm
# pbar = tqdm(total = len(vendas_format['ID Loja']), position=0, leave=True)

# for i, item in enumerate(vendas_format['ID Loja']):     #alterar valor usando for
#     pbar.update()   #barra de carregamento
#     if item == 210:
#         vendas_format.loc[i, 'Quantidade Devolvida'] += 1

# yamal = vendas_format['ID Loja']==210     #exibir DataFrame com os valores atualizados
# qtd = vendas_format['Quantidade Devolvida']
# final = vendas_format[yamal & qtd]
# print(final)

# EXERCICIO 2:

servicos_df = pd.read_excel(r'BaseServiçosPrestados.xlsx')
clientes_df = pd.read_csv(r'CadastroClientes.csv', sep=';', encoding='utf-8', decimal=',')
funcionarios_df = pd.read_csv(r'CadastroFuncionarios.csv', sep=';', encoding='utf-8',decimal=',')

# FATURAMENTO TOTAL
# empty = 0
# for i, item in enumerate(servicos_df['Tempo Total de Contrato (Meses)']):
#     cli = clientes_df['Valor Contrato Mensal']
#     soma = item * cli[i]
#     empty += soma
# print('O faturamento total da empresa é de {:.2f}'.format(empty))

# GABARITO FATURAMENTO TOTAL
# uniao = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente','Valor Contrato Mensal']], on= 'ID Cliente')
# uniao['Faturamento'] = uniao['Tempo Total de Contrato (Meses)'] * uniao['Valor Contrato Mensal']
# print(uniao['Faturamento'].sum())


# GASTO TOTAL
# salario = float(funcionarios_df['Salario Base'].sum())
# imposto = funcionarios_df['Impostos'].sum()
# beneficio = funcionarios_df['Beneficios'].sum()
# vt = float(funcionarios_df['VT'].sum())
# vr = funcionarios_df['VR'].sum()
# total = salario + imposto + beneficio + vt + vr
# print('O gasto total com funcionários é de {:.2f}'.format(total))

#GABARITO GASTO TOTAL
# funcionarios_df['Total de Gastos'] = funcionarios_df['Impostos'] + funcionarios_df['VR'] + funcionarios_df['VT'] + funcionarios_df['Beneficios'] + funcionarios_df['Salario Base']
# print('O gasto total com funcionários é de R${:,}'.format(funcionarios_df['Total de Gastos'].sum()))

# % CONTRATO FECHADO
# servicos_fd = len(servicos_df['ID Funcionário'].unique())
# print('{:.2%} de funcionários já fechou algum contrato'.format(servicos_fd/len(funcionarios_df['ID Funcionário'])))


# QUANTIDADE CONTRATOS POR ÁREA
# uniao = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on= 'ID Funcionário')
# uniao2 =uniao['Area'].value_counts()
# print(uniao2)
# uniao2.plot(kind='bar')
# plt.show()

# QUANTIDADE FUNCIONÁRIOS POR ÁREA
# funcionarios_df = funcionarios_df['Area'].value_counts()
# print(funcionarios_df.sum())
# funcionarios_df.plot(kind='bar')
# plt.show()

# TICKET MEDIO
# print(clientes_df)
# media = clientes_df['Valor Contrato Mensal'].mean()
# print('Media é R${:,.2f}'.format(media))
