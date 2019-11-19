#-*- coding: utf-8 -*-
from lista import Lista 
from datetime import date

'''
Arquivo com a classe Candidato()
'''
class Candidato:
    def __init__(self):
        self.__id_cand = int()
        self.__cpf_cand = int()
        self.__nome_cand = str()
        self.__sexo_cand = str()
        self.__data_nasc = str()
        self.__mun_nasc = str()
        self.__uf_nasc = str()
        self.__estado_civil = str()
        self.__grau_instr = str()
        self.__ano_eleicao = str()
        self.__num_partido = int()
        self.__nome_partido = str()
        self.__sigla_partido = str()
        self.__sigla_uf = str()
        self.__cod_cargo = int()
        self.__desc_cargo = str()
        self.__num_urna = int()
        self.__nome_urna = str()
        self.__cod_ocupacao = int()
        self.__desc_ocupacao = str()
        self.__sit_pos_pleito = str()
        self.__sit_candidatura = str()
        self.__bens = Lista()

    def getID(self):
        return self.__id_cand
    def setID(self, id):
        self.__id_cand = id
    
    def getCPF(self):
        return self.__cpf_cand
    def setCPF(self, cpf):
        self.__cpf_cand = cpf
    
    def getNome(self):
        return self.__nome_cand
    def setNome(self, nome):
        self.__nome_cand = nome
    
    def getSexo(self):
        return self.__sexo_cand
    def setSexo(self, sexo):
        self.__sexo_cand = sexo
    
    def getDataNasc(self):
        return self.__data_nasc
    def setDataNasc(self, data_nasc):
        self.__data_nasc = date.strftime(data_nasc, '%d/%m/%Y')
    
    def getMunNasc(self):
        return self.__mun_nasc
    def setMunNasc(self, municipio):
        self.__mun_nasc = municipio
    
    def getUFNasc(self):
        return self.__uf_nasc
    def setUFNasc(self, uf):
        self.__uf_nasc = uf
    
    def getEstadoCivil(self):
        return self.__estado_civil
    def setEstadoCivil(self, estado_civil):
        self.__estado_civil = estado_civil
    
    def getGrauInstr(self):
        return self.__grau_instr
    def setGrauInstr(self, grau_instr):
        self.__estado_civil = grau_instr
    
    def getAnoEleicao(self):
        return self.__ano_eleicao
    def setAnoEleicao(self, ano):
        self.__ano_eleicao = date.strftime(ano, '%Y')
    
    def getNumPartido(self):
        return self.__num_partido
    def setNumPartido(self, num_partido):
        self.__num_partido = num_partido
    
    def getPartido(self):
        return self.__nome_partido
    def setPartido(self, partido):
        self.__nome_partido = partido
    
    def getSiglaPartido(self):
        return self.__sigla_partido
    def setSiglaPartido(self, sigla):
        self.__sigla_partido = sigla
    
    def getUFPartido(self):
        return self.__sigla_uf
    def setUFPartido(self, sigla):
        self.__sigla_uf = sigla
    
    def getCodCargo(self):
        return self.__cod_cargo
    def setCodCargo(self, codigo):
        self.__cod_cargo = codigo
    
    def getDescCargo(self):
        return self.__desc_cargo
    def setDescCargo(self, descricao):
        self.__desc_cargo = descricao
    
    def getNumUrna(self):
        return self.__num_urna
    def setNumUrna(self, numero):
        self.__num_urna = numero
    
    def getNomeUrna(self):
        return self.__nome_urna
    def setNomeUrna(self, nome):
        self.__nome_urna = nome
    
    def getCodOcupacao(self):
        return self.__cod_ocupacao
    def setCodOcupacao(self, codigo):
        self.__cod_ocupacao = codigo
    
    def getDescOcupacao(self):
        return self.__desc_ocupacao
    def setDescOcupacao(self, descricao):
        self.__desc_ocupacao = descricao
    
    def getSituacaoPosPleito(self):
        return self.__sit_pos_pleito
    def setSituacaoPosPleito(self, situacao):
        self.__sit_pos_pleito = situacao
    
    def getCandidatura(self):
        return self.__sit_candidatura
    def setCandidatura(self, candidatura):
        self.__sit_candidatura = candidatura
    
    def getBens(self):
        return self.__bens
    def incluirBens(self, bem):
        self.__bens.Inserir(bem)
    
    '''
    def valor_bens(self):
        valor = float()
        for i in range(len(self.__bens)):
            valor += self.__bens[i].getValor()
        return valor
    '''

    def __str__(self):
        saida = str()
        saida += 'Candidato: {}\n' .format(self.__nome_cand) 
        saida += '{} -- {} -- {}\n' .format(self.__nome_urna, str(self.__num_urna), self.__sigla_partido)
        saida += '{} ({}) {} ({})\n' .format(self.__desc_cargo, self.__sigla_uf, self.__mun_nasc, self.__uf_nasc)
        saida += 'Resumo dos bens:\n'
        saida += '  - Total declarado: R$\n'
        saida += '  - Total por tipo de bem: R$'

        return saida
    
    def __repr__(self):
       return str((self.__id_cand, self.__cpf_cand, self.__nome_cand, self.__sexo_cand, 
       self.__data_nasc, self.__mun_nasc, self.__uf_nasc, self.__estado_civil, self.__grau_instr, 
       self.__ano_eleicao, self.__num_partido, self.__nome_partido, self.__sigla_partido, self.__sigla_uf, 
       self.__cod_cargo, self.__desc_cargo, self.__num_urna, self.__nome_urna, self.__cod_ocupacao, 
       self.__desc_ocupacao, self.__sit_pos_pleito, self.__sit_candidatura, self.__bens))