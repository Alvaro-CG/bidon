# test bidon
def perimetre(cote1, cote2, cote3):
    return (cote1 + cote2 + cote3)


if __name__ == "__main__":

    #     cote1, cote2, cote3 = 3, 2, 5
    cote1 = float(input('côté1 : '))
    cote2 = float(input('côté2 : '))
    cote3 = float(input('côté3 : '))
    perimetro = perimetre(cote1, cote2, cote3)
    print(f"Le perimetre du triangle est {perimetro}")