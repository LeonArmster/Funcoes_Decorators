# Função de soma
def soma(a:int, b:int)-> int:
    """
    Função com objetivo de calcular a soma de dois números inteiros
    """
    c = a+b
    return c

print(soma(5,6))


# Função par ou impar
def par_impar(a:int) -> str:
    """
    Função com objetivo de informar se o valor informado é par ou impar
    """
    c = a%2
    if c == 0:
        print('par')
    else:
        print('impar')


par_impar(4)


def calcular_fatorial(fatorial:int) -> int:
    """
    Função com o objetivo de calcular o fatorial do número informado
    """
    resultado = 1
    for x in range(1,fatorial+1):
        resultado *= x
    return resultado

print(calcular_fatorial(6))

help(calcular_fatorial)