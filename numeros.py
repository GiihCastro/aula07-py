def checarParOuImpar(numero:float):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def checarPositivoNegativoNeutro(numero:float):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "neutro"


def checarMaior(lista_de_numeros:list):
    if len(lista_de_numeros) == 0:
        return "Lista vazia"
    else:
        maior_item_da_lista = lista_de_numeros[0]
        for numero_da_vez in lista_de_numeros:
            if numero_da_vez > maior_item_da_lista:
                maior_item_da_lista = numero_da_vez
            return maior_item_da_lista


def checarMenor(lista_de_numeros:list):
    if len(lista_de_numeros) == 0:
        return "Lista vazia"
    else:
        menor_item_da_lista = lista_de_numeros[0]
        for numero_da_vez in lista_de_numeros:
            if numero_da_vez < menor_item_da_lista:
                menor_item_da_lista = numero_da_vez
            return menor_item_da_lista



def checarMedia(lista_de_numeros:list):
    if len(lista_de_numeros) == 0:
        return "Lista vazia"
    else:
        soma_total = 0
        for numero_da_vez in lista_de_numeros:
            soma_total += numero_da_vez
        media = soma_total / len(lista_de_numeros)
        return media