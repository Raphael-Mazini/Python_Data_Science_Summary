def fatorial(n=0):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n=0):
    return n*2



def triplo(n=0):
    return n*3


def str_moeda(preco=0, moeda='R$'):
    return f'{str_moeda}{preco}'.replace('.', ',')  