#-*- coding: utf-8 -*-
'''
Arquivo com a classe Controle()
'''
from view import Lista
from models import Candidato, Bem

class Controle:
    def __init__(self):
        self.__lista_cand = Lista()
        self.__lista_bens = Lista()

    def carregar_candidatos(self, arquivos):
        '''
        Carrega os candidatos a partir de um arquivo e os armazena em objetos do tipo Candidato(),
        esses objetos sao armazenados em uma classe Lista()
        '''
        dic_bens = dict()
        
        for arquivo in arquivos:
            with open(arquivo,'r', encoding='utf-8') as f:
                f.readline()
                for l in f.readlines():
                    l = l.replace('\n','')
                    l = l.replace('"','')
                    l = l.split(';')

                    candidato = Candidato()
                    candidato.setAnoEleicao(int(l[2]))
                    candidato.setUF(l[10])
                    candidato.setCodCargo(int(l[13]))
                    candidato.setDescCargo(l[14])
                    candidato.setID(int(l[15]))
                    candidato.setNumUrna(int(l[16]))
                    candidato.setNome(l[17])
                    candidato.setNomeUrna(l[18])
                    candidato.setCPF(int(l[20]))
                    candidato.setCandidatura(l[25])
                    candidato.setNumPartido(int(l[27]))
                    candidato.setSiglaPartido(l[28])
                    candidato.setPartido(l[29])
                    candidato.setUFNasc(l[35])
                    candidato.setMunNasc(l[37])
                    candidato.setDataNasc(l[38])
                    candidato.setSexo(l[42])
                    candidato.setGrauInstr(l[44])
                    candidato.setEstadoCivil(l[46])
                    candidato.setCodOcupacao(int(l[49]))
                    candidato.setDescOcupacao(l[50])
                    candidato.setSituacaoPosPleito(l[54])

                    for bem in self.__lista_bens:
                        if bem.getCandidato() == candidato.getID():
                            candidato.incluirBens(bem)

                    self.__lista_cand.Inserir(candidato)

                f.close()
        del dic_bens

    def carregar_bens(self, arquivos):
        '''
        Carrega os bens dos candidatos a partir de um arquivo e os armazena em objetos do tipo Bem(),
        esses objetos sao armazenados em uma classe Lista()
        '''
        for arquivo in arquivos:
            with open(arquivo,'r', encoding='utf-8') as f:
                f.readline()
                for l in f.readlines():
                    l = l.replace('\n','')
                    l = l.replace('"','')
                    l = l.split(';')

                    bem = Bem()
                    bem.setCandidato(int(l[11]))
                    bem.setCodigo(int(l[13]))
                    bem.setDescTipo(l[14])
                    bem.setDescBem(l[15])
                    bem.setValor(float(l[16].replace(',','.')))
                    self.__lista_bens.Inserir(bem)

                f.close()
    
    def recuperar_lista(self, partido=True, uf=False, mun_nasc=False, cargo=False, valor_bens=False, sit_pos_pleito=False):
        '''
        Retorna os candidatos de acordo com certas condicoes
        '''
        lista = Lista()
        if partido:
            sigla_partido = input('\nDigite a sigla do partido: ')
            for candidato in self.__lista_cand:
                if candidato.getSiglaPartido() == sigla_partido:
                    lista.Inserir(candidato)
        elif uf:
            sigla_uf = input('\nDigite a sigla da uf: ')
            for candidato in self.__lista_cand:
                if candidato.getUF() == sigla_uf:
                    lista.Inserir(candidato)
        elif mun_nasc:
            municipio = input('\nDigite o municipio: ')
            for candidato in self.__lista_cand:
                if candidato.getMunNasc() == municipio:
                    lista.Inserir(candidato)
        elif cargo:
            desc_cargo = input('\nDigite o cargo: ')
            for candidato in self.__lista_cand:
                if candidato.getDescCargo() == desc_cargo:
                    lista.Inserir(candidato)
        elif valor_bens:
            valor = float(input('\nDigite o valor total dos bens: '))
            for candidato in self.__lista_cand:
                if candidato.valorBens() > valor:
                    lista.Inserir(candidato)
        elif sit_pos_pleito:
            situacao = input('\nDigite uma situacao pos pleito: ')
            for candidato in self.__lista_cand:
                if candidato.getSituacaoPosPleito() == situacao:
                    self.__lista_cand.Inserir(candidato)
        else:
            raise ValueError('Pelo menos 1 parametro True')
        return lista

    def exibir_lista(self, lista):
        '''
        Exibi a lista obtida no metodo lista_candidatos()
        '''
        if len(lista) == 0:
            raise IndexError('Lista vazia')
        else:
            for candidado in lista:
                print('\n', candidado)

    def media_bens(self, cargo=True, uf=False, partido=False, ocupacao=False, ano_nascimento=False):
        '''
        Mostra amostram a media do total de bens dos candidatos por cargo, UF, partido, ocupacao, 
        ou ano de nascimento.
        '''
        media = float()
        bens = int()
        if cargo:
            print('\nMedia de bens por cargo: ', end='')
            lista_cargos = list()
            for candidato in self.__lista_cand:
                if candidato.getDescCargo() not in lista_cargos:
                    bens += len(candidato.getBens())
                    lista_cargos.append(candidato.getDescCargo())
            media = bens/len(lista_cargos)
        elif uf:
            lista_uf = list()
            print('\nMedia de bens por UF: ', end='')
            for candidato in self.__lista_cand:
                if candidato.getUF() not in lista_uf:
                    bens += len(candidato.getBens())
                    lista_uf.append(candidato.getUF())
            media = bens/len(lista_uf)
        elif partido:
            print('\nMedia de bens por partido: ', end='')
            lista_partido = list()
            for candidato in self.__lista_cand:
                if candidato.getSiglaPartido() not in lista_partido:
                    bens += len(candidato.getBens())
                    lista_partido.append(candidato.getSiglaPartido())
            media = bens/len(lista_partido)
        elif ocupacao:
            print('\nMedia de bens por ocupacao: ', end='')
            lista_ocupacao = list()
            for candidato in self.__lista_cand:
                if candidato.getDescOcupacao() not in lista_ocupacao:
                    bens += len(candidato.getBens())
                    lista_ocupacao.append(candidato.getDescOcupacao())
            media = bens/len(lista_ocupacao)
        elif ano_nascimento:
            print('\nMedia de bens por ano de nascimento: ', end='')
            lista_ano = list()
            for candidato in self.__lista_cand:
                if candidato.getDataNasc() not in lista_ano:
                    bens += len(candidato.getBens())
                    lista_ano.append(candidato.getDataNasc())
            media = bens/len(lista_ano)
        else:
            raise ValueError('Pelo menos 1 parametro True')

        return media

    def remover(self, candidatura=True, sit_pos_pleito=False):
        '''
        Funcao que remove da lista todos os candidatos que satisfacam um critério.
        '''
        if candidatura:
            for candidato in self.__lista_cand:
                if candidato.getCandidatura() == 'INDEFERIDO':
                    self.__lista_cand.Remover(candidato)
        elif sit_pos_pleito:
            for candidato in self.__lista_cand:
                if candidato.getSituacaoPosPleito() != 'ELEITO':
                    self.__lista_cand.Remover(candidato)
        else:
            raise ValueError('Pelo menos 1 parametro True')