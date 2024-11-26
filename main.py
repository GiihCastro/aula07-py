from letras import contarPalavras, contarConsoantes, contarVogais

palavra = input("Digite uma palavra: ")
qtde_consoantes = contarConsoantes(palavra=palavra)
qtde_vogais = contarVogais(palavra=palavra)
print(f"Seu nome tem {qtde_consoantes} consoantes e {qtde_vogais} vogais.")

frase = input("Digite uma frase: ")
qtde_palavras = contarPalavras(frase=frase)
print(f"Sua frase tem {qtde_palavras} palavras.")

