# -*- coding: utf-8 -*-

# Pyseab - Simplificador de Expressões Algébricas Booleanas

#Copyright (c) 2013 jpbanczek@gmail.com
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#The views and conclusions contained in the software and documentation are those
#of the authors and should not be interpreted as representing official policies,
#either expressed or implied, of the FreeBSD Project.

__author__ = "Jhonathan Paulo Banczek (jpbanczek@gmail.com)"
__copyright__ = "Copyright (C) 2013 Jhonathan Paulo Banczek"
__license__ = "New BSD License"

class PySeab(object):

    def __init__(self):

        self.expressao = None

    def _analise_Lexica(self):
        """ Efetua a análise léxica, retorno: True, False """

        letras = set('ABCDEFGHIJKLMNOPQRSTUVXZWY')
        alf = set('X.+~()')

        for i in self.expressao:
            if i in alf or i in letras:
                pass
            else:
                return False

        return True


    def _balanceamento(self):
        """
        verifica se os parentes estão balanceados
        retorno: True, False
        """
        return self.expressao.count('(') == self.expressao.count(')')


    def _analise_Sintatica(self):
        """ Efetua a análise sintática, retorno: True, False """

        flag = True
        letras = 'ABCDEFGHIJKLMNOPQRSTUVXZWY'
        aux = self.expressao

        #conjunto de caracteres nao permitidos
        np = ['00', '01', '03', '12', '14', '22', '24', '32', '34',
         '40', '41', '43']

        #Substitui os valores originais, por números inteiro [Godel]
        aux = aux.replace('~','1')
        aux = aux.replace('.','2')
        aux = aux.replace('+','2')
        aux = aux.replace('(','3')
        aux = aux.replace(')','4')

        #subistitui todas as letras da expressão pelo número '0'
        for i in letras:
            aux = aux.replace(i,'0')

        # Inicio da análise
        # Se iniciar com '+' ou '.' ou ')' = inconsistente (2, 4)
        # Se terminar com '+' ou '.' ou '~' ou '(' = inconsistente (1, 2, 3).
        if (aux.startswith('2') is True or aux.startswith('4') is True or
            aux.endswith('1') is True or aux.endswith('2') is True or
            aux.endswith('3') is True):
            flag = False

        #verifica se a expressão contem os caracteres não permitidos
        for i in np:
            if aux.find(i) != -1:
                flag = False
                break

        return flag


    def _simplificacao(self):
        """ simplica a expressão original """

        pass


    def analise( self ):
        """
        executa a análise léxica, balanceamento de parenteses
        e a análise sintátca.
        """

        self.expressao = self.expressao.upper()
        self.expressao = self.expressao.strip()
        self.expressao = self.expressao.replace(' ', '')

        if self.expressao == '':
            print('expressao vazia')

        else:
            flag_analise = [' -> Analise Léxica Consistente;\n', #0
            ' -> Balanceamento Consistente;\n"',                 #1
            ' -> Análise Sintática Consistente;\n',              #2
            ' -> Análise Léxica com INCONSISTENCIA;\n',          #3
            ' -> Balanceamento com INCONSISTENCIA;\n',           #4
            ' -> Análise Sintática com INCONSISTENCIA;\n']       #5

            resp = []

            if self._analise_Lexica() == True:
                resp.append(0)
                if self._balanceamento() == True:
                    resp.append(1)
                    if self._analise_Sintatica() == True:
                        resp.append(2)
                    else:
                        resp.append(5)
                else:
                    resp.append(4)
            else:
                resp.append(3)

            #saida, resposta da analise
            for i in resp:
                print(flag_analise[i])