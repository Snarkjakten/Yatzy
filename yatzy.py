# python 3.6
import random
import numpy
s = 0
tur = 1
while True:

    if s < 1:
        """ skapar matris som ska bli scoreboard for s antal spelare"""
        print("Nytt spel")
        s = int(input("Hur manga spelare spelar?"))
        numpy.set_printoptions(threshold=numpy.nan)
        scoreboard = numpy.zeros((7, s+1))

        """ fixar poangkategorier i scoreboard """
        x = 7
        for x in range(7):
            scoreboard[x, 0] = x
            x += 1

        """" fixar spelarkolumnen i scoreboard """
        x = 1
        for x in range(s+1):
            scoreboard[0, x] = x
            x += 1
        print(scoreboard)

    def kast(tur):

        """ kastar n tarningar som sparas i en lista """
        dielist = []
        x = 0
        n = int(input("hur manga tarningar vill du kasta?"))
        for x in range(n):  # x < n
            kast = random.randint(1,6)
            dielist.append(kast)
        print(dielist)

        """ kastar om utvalda tarningar, 2 ggr, uppdaterar listan """
        x = 0
        for x in range(2):
            omkast = input("vilka tarningar vill du kasta om?")
            omkast = omkast.split()
            k = 0
            for x in range(len(omkast)):
                dielist[int(omkast[k])-1] = random.randint(1, 6)
                k += 1
            print(dielist)
            x += 1

        """ valjer vilka siffror man vill spara och summerar dem """
        spara = int(input("vad vill du spara?"))
        x = 0
        count = 0
        for x in range(len(dielist)):
            if dielist[x] == spara:
                count += 1
        print("Summan ar", count*spara)

        scoreboard[spara, tur] = count*spara

        print(scoreboard)
        return scoreboard
    y = 0
    for y in range(6):
        tur = 1
        x = 0
        for x in range(s):
            scoreboard = kast(tur)
            tur += 1
            print("Nasta spelares tur")
    s = 0
    print("spelet r slut")
