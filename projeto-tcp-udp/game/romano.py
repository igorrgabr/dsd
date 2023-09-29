def int_romano(numero):
    val = [10, 9, 5, 4, 1]
    syb = ["X", "IX", "V", "IV", "I"]

    romano = ""
    i = 0
    while numero > 0:
        for _ in range(numero // val[i]):
            romano += syb[i]
            numero -= val[i]
        i += 1

    return romano