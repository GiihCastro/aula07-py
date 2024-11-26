def contarVogais(palavra:str): 
    vogais = "aeiouáàãâéèêíóôõú"
    contador = 0
    for letra_da_vez in palavra:
        if letra_da_vez.lower() in vogais:
            contador += 1
    return contador

def contarConsoantes(palavra:str):
    consoantes = "bcdfghjklmnpqrstvxywz"
    contador = 0
    for caractere_da_vez in palavra:
        if caractere_da_vez.lower() in consoantes:
            contador += 1
    return contador

def contarPalavras(frase:str):
    contador = 1
    for palavra_da_vez in frase.strip():
        if palavra_da_vez == " ":
            contador += 1
    return contador

def transformarMai(palavra):
    return palavra.upper()

def transformarMin(palavra):
    return palavra.lower()
