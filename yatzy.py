# python 3.6
import random
import numpy
while True:

    """ skapar matris som ska bli scoreboard for s antal spelare"""
    """ Jag gillar glass"""
    s = int(input("Hur manga spelare spelar?"))
    numpy.set_printoptions(threshold=numpy.nan)
    scoreboard = numpy.zeros((7, s+1))

    """ fixar poangkategorier i scoreboard """
    x = 1
    for x in range(7):
        scoreboard[x, 0] = x
        x += 1
    print(scoreboard)

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

    print("Nasta spelares tur")
