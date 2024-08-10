# TXT:

# ler arquivo txt
# arquivo = open(r"C:\Users\leand\OneDrive\Documentos\hashtag\f_data\pdf_e_txt\Alunos.txt", 'r') #'r' = ler, 'a'= adicionar/editar, 'w' = escrever do zero 
# ler = arquivo.read()
# print(ler)

# criar novo arquivo e escrever nele
# with open('Brainless.txt', 'w') as arquivo2:
#     arquivo2.write('Brainless aqui')

# PDF:

# manusear pdf
import PyPDF2 as pyf
# manusear caminhos e pastas do pc
from pathlib import Path
# manusear tabelas em pdf
import pandas as pd
# from tabula import wrapper
# # import tabula
# from tabula.io import read_pdf
# from tabula import 

# # abrir arquivo
# arquivo = 'MGLU_ER_4T20_POR.pdf'
# arquivo_pdf = pyf.PdfReader(arquivo)

# # descompactar um pdf em várias cópias iguais de paginas pdf
# I = 1
# for pagina in arquivo_pdf.pages:
#     new_archive = pyf.PdfWriter()  #abrindo um novo arquivo do zero
#     new_archive.add_page(pagina)

#     # salvar o arquivo no local específico 
#     with Path(f'f_data/archive{I}.pdf').open(mode='wb') as final_archive:
#         new_archive.write(final_archive)
#         I += 1



# adicionar múltiplos pdfs em 1 pdf principal
# pag_pdfs = [1, 14, 16]
# new_pdf = pyf.PdfWriter()

# for num in pag_pdfs:
#     local = (f'f_data/archive{num}.pdf') #identificar local do arquivo
#     reading = pyf.PdfReader(local) #ler o primeiro arquivo pdf
#     pag_arq_pdf = reading.pages[0] #indicar qual página do pdf vou querer adicionar
#     new_pdf.add_page(pag_arq_pdf) #adicionar paginas no pdf principal

# # salvar 
# with Path(f'arquivo_principal.pdf').open(mode='wb') as finish: #"salve tudo que foi digitado acima
#         new_pdf.write(finish) #e escreva no meu new_pdf"


# mesclar dois PDFs inteiros:
# pdf_mesclado = pyf.PdfMerger()
# pdf1 = 'MGLU_ER_3T20_POR.pdf'
# pdf2 = 'MGLU_ER_4T20_POR.pdf'

# pdf_mesclado.append(pdf1)
# pdf_mesclado.append(pdf2)

# with Path(f'mescladão.pdf').open(mode='wb') as arquivo_final:
#     pdf_mesclado.write(arquivo_final)


# adicionar um pdf inteiro no meio de outro pdf
# pdf_mesclado = pyf.PdfMerger()
# pdf1 = 'MGLU_ER_3T20_POR.pdf'
# pdf2 = 'MGLU_ER_4T20_POR.pdf'

# pdf_mesclado.append(pdf1)
# pdf_mesclado.merge(1, pdf2) #adicionar pdf2 depois da página 1

# with Path(f'mergezao.pdf').open(mode='wb') as arquivo_final:
#     pdf_mesclado.write(arquivo_final)


# rotacionar página do pdf
# pdf_aux = pyf.PdfReader(pdf1)

# pdf_rotate = pyf.PdfWriter()
# for pagina in pdf_aux.pages:
#     pagina.rotate(90)
#     pdf_rotate.add_page(pagina)

# with Path(f'rotacionado.pdf').open(mode='wb') as final_archive:
#     pdf_rotate.write(final_archive)


# exibir número total de páginas
# read = pyf.PdfReader(pdf1)
# num_pag = len(read.pages)
# print(num_pag)

# extrair informações do texto
# informações = read.metadata
# print(informações)
    
# extrair texto dentro do pdf
# read = pyf.PdfReader(pdf1)
# texto_requerido = '| Despesas com Vendas'

# i = 1
# for pag in read.pages:
#     texto_pag = pag.extract_text() #extrair textos das páginas
#     if texto_requerido in texto_pag:
#         print(f'Texto se encontra na página {i}')
#         texto_bruto = texto_pag  #apenas salvar após encontrar o texto requerido
#         pag_final = i  #apenas salvar após encontrar página requerida
#     i += 1
# # localizar onde começa e termina o texto requerido
# local1 = texto_bruto.find('| Despesas com Vendas')
# local2 = texto_bruto.find('|', local1 + 1)   #(str procurada, a partir de onde começará a procura)
# # extrair texto no local exato
# texto_final = texto_bruto[local1:local2]
# print(texto_final)


# extrair tabelas pdf
# df = tabula.wrapper(pdf1, page=5)