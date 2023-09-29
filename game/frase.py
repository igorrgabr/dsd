import random

def frase_aleatoria():
    subst = ["A vida", "A morte", "O segredo", "O destino", "A névoa", "O enigma"]
    verbo = ["sussura", "submerge", "deleita", "encanta", "oculta", "revela"]
    compl = ["no olhar enigmático", "no silêncio", "atrás da porta", "o paradoxo do tempo", "os segredos", "o desconhecido"]

    frase = [random.choice(subst), random.choice(verbo), random.choice(compl)]

    return frase