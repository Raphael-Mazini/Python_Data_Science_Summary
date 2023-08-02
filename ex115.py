


def linha(tam=42):
    return ('=' * tam)



def cabecalho(txt):
    print(linha()) 
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    print(lista)    