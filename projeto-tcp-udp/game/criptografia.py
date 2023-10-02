def criptografar(texto, deslocamento):
    texto_cifrado = ""

    for char in texto:
        if char.isalpha():
            maiuscula = char.isupper()
            char = char.lower()
            indice = ord(char) - ord('a') # calcula a posição da letra no alfabeto
            novo_indice = (indice + deslocamento) % 26 # aplica o deslocamento na letra
            novo_char = chr(novo_indice + ord('a')) # converte o novo indice de volta para um caractere
            
            if maiuscula:
                novo_char = novo_char.upper()
                
            texto_cifrado += novo_char
        else:
            texto_cifrado += char
    
    return texto_cifrado

def descriptografar(texto_cifrado, deslocamento):
    texto_original = ""

    for char in texto_cifrado:
        if char.isalpha():
            maiuscula = char.isupper()
            char = char.lower()
            indice = ord(char) - ord('a')
            novo_indice = (indice - deslocamento) % 26
            novo_char = chr(novo_indice + ord('a'))

            if maiuscula:
                novo_char = novo_char.upper()

            texto_original += novo_char
        else:
            texto_original += char
    
    return texto_original