#-*- coding: utf-8 -*-
'''
Arquivo com a classe Candidato(), Bem() e Cronometro()
'''
from view import Lista 
import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

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
        self.__data_nasc = data_nasc
    
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
        self.__ano_eleicao = ano
    
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
    
    def getUF(self):
        return self.__sigla_uf
    def setUF(self, sigla):
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
    
    def valorBens(self):
        '''
        Retorna o valor total dos bens do candidato
        '''
        valor = float()
        for bem in self.__bens:
            valor += bem.getValor()
        return valor
    
    def valorTipo(self):
        '''
        Retorna o valor por tipo de bem do candidato
        '''
        if not self.__bens is None:
            saida = str()
            dic_valores = dict()
            for bem in self.__bens:
                if bem.getCodigo() not in dic_valores.keys():
                    dic_valores[bem.getCodigo()] = bem.getValor()
                else:
                    dic_valores[bem.getCodigo()] += bem.getValor()

            for codigo, valor in dic_valores.items():
                saida += '{}: {} \t' . format(codigo, locale.currency(valor, grouping=True))
            
            del dic_valores
            return saida
        else:
            return 'R$'
    
    def __getTipo(self, no):
        '''
        Verifica se o tipo do objeto e o mesmo
        '''
        if type(self) == type(no):
            return True
        else:
            raise TypeError('Tipos diferentes de objetos')
    
    #Metodos comparativos
    def __lt__(self, no):
        if self.__getTipo(no):
            return self.__id_cand < no.getID()

    def __gt__(self, no):
        if self.__getTipo(no):
            return self.__id_cand > no.getID()
    
    def __le__(self, no):
        if self.__getTipo(no):
            return self.__id_cand <= no.getID()
    
    def __ge__(self, no):
        if self.__getTipo(no):
            return self.__id_cand >= no.getID()
    
    def __eq__(self, no):
        if self.__getTipo(no):
            return self.__id_cand == no.getID()
    
    def __ne__(self, no):
        if self.__getTipo(no):
            return self.__id_cand != no.getID()
            
    def __str__(self):
        saida = str()
        saida += '{} -- {} -- {}\n' .format(self.__nome_urna, str(self.__num_urna), self.__sigla_partido)
        saida += '{} ({}) {} ({})\n' .format(self.__desc_cargo, self.__sigla_uf, self.__mun_nasc, self.__uf_nasc)
        saida += 'Resumo dos bens:\n'
        saida += '  - Total declarado: {}\n' .format(locale.currency(self.valorBens(), grouping=True))
        saida += '  - Total por tipo de bem -> {}' .format(self.valorTipo())

        return saida
    
    def __repr__(self):
       return str((self.__id_cand, self.__cpf_cand, self.__nome_cand, self.__sexo_cand, 
       self.__data_nasc, self.__mun_nasc, self.__uf_nasc, self.__estado_civil, self.__grau_instr, 
       self.__ano_eleicao, self.__num_partido, self.__nome_partido, self.__sigla_partido, self.__sigla_uf, 
       self.__cod_cargo, self.__desc_cargo, self.__num_urna, self.__nome_urna, self.__cod_ocupacao, 
       self.__desc_ocupacao, self.__sit_pos_pleito, self.__sit_candidatura, self.__bens))

class Bem:
    def __init__(self):
        self.__cod_tipo = int()
        self.__desc_tipo = str()
        self.__candidato = int()
        self.__desc_bem = str()
        self.__valor = float()
    
    def getCodigo(self):
        return self.__cod_tipo
    def setCodigo(self, codigo):
        self.__cod_tipo = int(codigo)
    
    def getDescTipo(self):
        return self.__desc_tipo
    def setDescTipo(self, descricao):
        self.__desc_tipo = descricao

    def getCandidato(self):
        return self.__candidato
    def setCandidato(self, candidato):
        self.__candidato = int(candidato)

    def getDescBem(self):
        return self.__desc_bem
    def setDescBem(self, descricao):
        self.__desc_bem = descricao
    
    def getValor(self):
        return self.__valor
    def setValor(self, valor):
        self.__valor = valor
    
    def __str__(self):
        saida = 'Candidato: %i\n' % self.__candidato
        saida += '{} -- {} -- {} -- Descricao: {}' .format(self.__cod_tipo, self.__desc_tipo, locale.currency(self.__valor, grouping=True), self.__desc_bem)
        return saida
    
    def __repr__(self):
        atributos = (self.__cod_tipo, self.__desc_tipo, self.__valor, self.__desc_bem)
        return str(atributos)
    
    def __getTipo(self, outro):
        if type(self) == type(outro):
            return True
        else:
            raise TypeError('Operacao nao suportada entre as instancias dos objetos')

    def __lt__(self, bem):
        if self.__getTipo(bem):
            return (self.__valor < bem.getValor() or self.__cod_tipo < bem.getCodigo() or self.__desc_bem < bem.getDescBem())

    def __gt__(self, bem):
        if self.__getTipo(bem):
            return (self.__valor > bem.getValor() or self.__cod_tipo > bem.getCodigo() or self.__desc_bem > bem.getDescBem())
    
    def __le__(self, bem):
        if self.__getTipo(bem):
            return (self.__valor <= bem.getValor() or self.__cod_tipo <= bem.getCodigo() or self.__desc_bem <= bem.getDescBem())
    
    def __ge__(self, bem):
        if self.__getTipo(bem):
            return (self.__valor >= bem.getValor() or self.__cod_tipo >= bem.getCodigo() or self.__desc_bem >= bem.getDescBem())
    
    def __eq__(self, bem):
        if self.__getTipo(bem):
            return ((self.__valor == bem.getValor()) and (self.__desc_bem == bem.getDescBem()))
           
    def __ne__(self, bem):
        if self.__getTipo(bem):
            return ((self.__valor != bem.getValor()) or (self.__desc_bem != bem.getDescBem()))