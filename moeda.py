def aumentar(preco=0, taxa=0, formato=False):
    aumet =  preco + (preco * (taxa / 100))
    porc = (preco * taxa) / 100
    return aumet, porc if formato is False else moeda(aumet)
    
    
def diminuir(preco=0, taxa=0, formato=False):
    dimi =  preco - (preco * (taxa / 100))
    porc = (preco * taxa) / 100
    return dimi, porc if formato is False else moeda(dimi)


def dobro(n=0, formato=False):
    resp =  n*2
    return resp if not formato else moeda(resp)



def triplo(n=0, formato=False):
    resp = n*3
    return resp if not formato else moeda(resp)


def metade(preco=0, formato=False):
    resp = preco / 2
    return resp if not formato else moeda(resp)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')
