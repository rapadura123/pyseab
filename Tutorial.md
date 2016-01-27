# Introdução: Exemplo de uso #

Considerando que tenha o Python 3 instalado e dentro de uma pasta, tenha o código "PySeab.py"

Crie um outro código "Teste.py" (dentro da mesma pasta)

com o seguinte conteúdo
```
#importa o módulo PySeab
from PySeab import PySeab

#cria uma função para testar as expressões
def teste():

    print("""\n\t Copyright (c) 2013 jpbanczek@gmail.com
        \tAll rights reserved.""")

    while True:
        exp = input("Entre com a Expressão: ")
        if exp == 'Sair':
           break
        else:
            p = PySeab()
            p.expressao = exp # passa o valor para o atributo
            p.analise()

if __name__ == "__main__":
    teste()
```


Para executar o código, navegue até a pasta onde o mesmo se encontra,
abra o terminal e digite:

```
>>> python3 Teste.py
```