#
##############################################################################
# PySeab - Simplificador de Expressões Algébricas Booleanas.
# Autor: Jhonathan Paulo Banczek
# Data: 07/03/2013
# Última Modificação: 17/05/2013 - 3,7
# google code - mercurial.
# Python 3.3.1 - Linux, Ubuntu 32 bit. 13.04
# -------------------------------------------------------------
#                       Implementações:
# 1 -> Alfabeto Reconhecido. (ok).
# 2 -> Análise Léxica. (ok)
# 3 -> Análise Sintática. <implementando>
# 5 -> Balanceamento dos Parênteses. <ok>
# 6 -> Classe Simp <implementando __init__>
# 7 -> Implementacao da analise sintatica (método tabela) <implementando>
#---------------------------------------------------------------|

class Simp( object ):

  def __init__( self, exp ):

    self.exp = exp

    # Alfabeto reconhecido com seu significado (dict)
    self.alf = {'A':['.','+',')'],'B':['.','+',')'],'C':['.','+',')'],
               'D':['.','+',')'],'E':['.','+',')'], 'F':['.','+',')'],
               'G':['.','+',')'],'H':['.','+',')'], 'I':['.','+',')'],
               'J':['.','+',')'],'K':['.','+',')'],'L':['.','+',')'],
               'M':['.','+',')'],'N':['.','+',')'],'O':['.','+',')'],
               'P':['.','+',')'],'Q':['.','+',')'],'R':['.','+',')'],
               'S':['.','+',')'],'T':['.','+',')'], 'U':['.','+',')'],
               'V':['.','+',')'],'X':['.','+',')'],'Z':['.','+',')'],
               'W':['.','+',')'], 'Y':['.','+',')'],'~':['x','(','~'],
                '+':['x','~','('], '.':['x','~','('], '(':['x','~','('],
                ')':['x','~',')']}

    # implementação da tabela de analise sintática
    self.alf2 = { 'X':{'X':'00' ,'.':'11' ,'+':'11' ,'~':'10',
                  '(':'10' ,')':'01'},
                '.':{'X':'11' ,'.':'00' , '+':'00' ,'~':'01' ,
                  '(':'01' ,')':'10'},
                '+':{'X':'11' ,'.':'00' ,'+':'00' ,'~':'01' ,
                  '(':'11' ,')':'00'},
                '~':{'X':'01' ,'.':'00' ,'+':'10' ,'~':'11' ,
                  '(':'11' ,')':'00'},
                '(':{'X':'01' ,'.':'10' ,'+':'10' ,'~':'01',
                  '(':'11' ,')':'00'},
                ')':{'X':'10' ,'.':'01' ,'+':'01' ,'~':'00',
                  '(':'00' ,')':'11'}}

# Método para Analise léxica.
# retorno: True, False
  def _analise_Lexica( self ):

    # flag variavel True se tiver tudo correto, caso contrario False
    flag = True

    # para cada caracter na formula, procure se existe no dict: alf
    # se não existir retorna: None
    for i in self.exp:
      if self.alf.get(i) == None:
        print('caracter: ' + i + " não suportado")
        flag = False
        break

    return flag

  # Método para Analise SIntática
  # retorno: True, False
  def _analise_Sintatica( self ):

    flag = True
    var = 'ABCDEFGHIJKLMNOPQRSTUVXZWY'

    for i in range( len(self.exp) ):
      for j in self.alf.get(self.exp[i]):

        if i == len(self.exp)-1:
          #print('se for ultimo numero')
          flag = True
          break

        elif j == 'x':
          #print('se for j for uma variavel')

          if var.find(self.exp[i+1]) == -1:
            #print('se o proximo caracter nao for uma letra')
            flag = False
          else:
            #print('é uma letra')
            flag = True
            break

        elif j == self.exp[i+1]:
          #print('entro no if caso j for igual ao proximo caracter')
          flag = True
          break
        else:
          #print('entro senao externo')
          flag = False

    return flag

  #------------------- analise sintatica 2 self.alf2--------------------
  def analise_sintatica2( self ):

    flag = True
    #var = 'ABCDEFGHIJKLMNOPQRSTUVXZWY'

    for i in range( len( self.exp ) ):

      # --- recebe o antecessor
      try:
        a = self.exp[i-1]
      except:
        a = self.exp[i]

      # --- recebe o sucessor
      try:
        s = self.exp[i+1]
      except:
        s = self.exp[i]

      if self.exp[i].isalpha() == True:
        pass



  def _balanceamento( self ):

    x = self.exp.count('(')
    y = self.exp.count(')')

    if x == y:
      return True
    else:
      return False

  def analise( self ):

    # converte pra maiusculo
    self.exp = self.exp.upper()
    # retira espaços no começo e no fim da string
    self.exp = self.exp.strip()
    # retira espaços no meio da string
    self.exp = self.exp.replace(' ', '')

    if self._analise_Lexica() == True:
      print("> Analise léxica -consistente-")

      if self._balanceamento() == True:
        print("> Balanceamento - consistente-")

        if self._analise_Sintatica() == True:
          print("> Analise Sintática -consistente-")
        else:
          print(" > analise sintática com INCONSISTENCIA")
      else:
         print(" > Balanceamento com INCONSISTENCIA")
    else:
      print(" > analise léxica com INCONSISTENCIA")
