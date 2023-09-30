import random

def frase_aleatoria():
    subst = ["A vida", "A morte", "O segredo", "O destino", "A nevoa", "O enigma"]
    verbo = ["sussura", "submerge", "deleita", "encanta", "oculta", "revela"]
    compl = ["no olhar enigmatico", "no silencio", "atras da porta", "o paradoxo do tempo", "os segredos", "o desconhecido"]

    return f"{random.choice(subst)} {random.choice(verbo)} {random.choice(compl)}"