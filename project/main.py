#-*- coding: utf-8 -*-
'''
Classe principal do programa
'''
from pathlib import Path
from control import Controle
from time import perf_counter

def gravar_tempos(caminho_arq, lista_tempos):
    with open(caminho_arq, 'a') as arquivo:
        arquivo.write('\n')
        for i in range(len(lista_tempos)):
            if i == len(lista_tempos):
                arquivo.write(str(round(lista_tempos[i],6)) + '\n')
            else:
                arquivo.write(str(round(lista_tempos[i],6)) + ';')
       
        arquivo.close()

def main():
    #Arquivos dos candidatos
    pasta_candidatos = Path('./dados/consulta_cand_2014')
    arquivos_candidatos = list(pasta_candidatos.glob('consulta_cand_2014_*.csv'))

    #Arquivos dos bens
    pasta_bens = Path('./dados/bem_candidato_2014')
    arquivos_bens = list(pasta_bens.glob('bem_candidato_2014_*.csv'))

    lista_tempos = list()
    main = Controle()

    #Carregar bens
    tempo_inicial = float(perf_counter())
    main.carregar_bens(arquivos_bens)
    tempo_final = float(perf_counter())
    tempo_total = tempo_final - tempo_inicial
    lista_tempos.append(tempo_total)

    #Carregar candidatos
    tempo_inicial = float(perf_counter())
    main.carregar_candidatos(arquivos_candidatos)
    tempo_final = float(perf_counter())
    tempo_total = tempo_final - tempo_inicial
    lista_tempos.append(tempo_total)

    #Recuperar lista
    tempo_inicial = float(perf_counter())
    lista_recuperada = main.recuperar_lista(False, True)
    tempo_final = float(perf_counter())
    tempo_total = tempo_final - tempo_inicial
    lista_tempos.append(tempo_total)

    #Exibir Candidatos
    tempo_inicial = float(perf_counter())
    print(main.exibir_lista(lista_recuperada))
    tempo_final = float(perf_counter())
    tempo_total = tempo_final - tempo_inicial
    lista_tempos.append(tempo_total)

    #Media dos bens
    tempo_inicial = float(perf_counter())
    print(main.media_bens())
    tempo_final = float(perf_counter())
    tempo_total = tempo_final - tempo_inicial
    lista_tempos.append(tempo_total)
    
    #Remover candidatos
    tempo_inicial = float(perf_counter())
    main.remover()
    tempo_final = float(perf_counter())
    tempo_total = tempo_final - tempo_inicial
    lista_tempos.append(tempo_total)
    
    gravar_tempos('./dados/tempos_de_execucao.csv', lista_tempos)
    
if __name__ == "__main__":
    main()