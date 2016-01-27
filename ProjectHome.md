PySeab - Simplificador de expressões Algébricas Booleanas

### Algoritmo com implementação em Python (versão 3.3) efetua a Análise Léxica, Balanceamento de Parênteses e Análise Sintática. ###

**Estado Atual:** Em desenvolvimento o método formal para a simplificação da Expressão.

**Objetivo:** Fornecer uma ferramenta para análise de um expressão booleana e gerar a sua
simplificação (minimização de função).

Tutorial de uso: https://code.google.com/p/pyseab/wiki/Tutorial


---


Requisitos básicos (Linux/Ubuntu):
Python 3.**instalado.**

No terminal digite:
```
sudo apt-get install python3
```

opcional
```
sudo apt-get install python3-all
```


---


### Alfabeto reconhecido: ###

  * **Varáveis:** A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,X,Z,W,Y (pode se usar minúsculo)

  * **Operador Unário:** ~ (negação, negado, NOT)

  * **Operadores Binário:** + (soma lógica, ou, OR)
  * . (multiplicação Lógica, E, AND)

  * **Delimitadores:** (, ) (Parênteses)


**Exemplo de Expressão aceita:**


>>> ( a + b ) . ~ ( ~ b . c ) # Ignora espaços em branco`


>>> (A+B).~(~B.C)             # não faz diferença entre letras Maiúsculas e minúsculas


>>> (((A+B).~(C)))



Os carácteres: **, {, }, !,- não são permitidos.**


---


**Sugestão de Implementação ou modificações contate:** jpbanczek@gmail.com


---


**Sobre o Autor:**  http://lattes.cnpq.br/1051351787984481



---


**Licença de Uso**: NEW BSD LICENSE


---



Copyright (c) 2013 jpbanczek@gmail.com All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.


2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the authors and should not be interpreted as representing official policies, either expressed or implied, of the FreeBSD Project.