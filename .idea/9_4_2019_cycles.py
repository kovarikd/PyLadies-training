# This files contains examples from Pyladies training
# Following thing is cycle exercise

from turtle import forward, left, right, exitonclick, penup, pendown, exitonclick
from random import randint

def dis_line():
    for i in range(15):
        penup()
        forward(5)
        pendown()
        forward(20)

    exitonclick()

def ext_line():
    for i in range(15):
        penup()
        forward(3)
        pendown()
        forward(i*3)

    exitonclick()

def three_squares():
    for i in range(3):
        for i in range(4):
            forward(100)
            left(90)
        left(20)
    exitonclick()

def stairs():
    for i in range(7):
        forward(50)
        left(90)
        forward(50)
        right(90)

    exitonclick
def asses_score(body):
    if body > 21:
        print("You've lost! {} is higher than 21.".format(body))
    else:
        print("You've Won! {} is lower than 21.".format(body))

def oko_bere():
    body = 0
    while True:
        print("Mas {} bodu!".format(body))
        odp = input("Chces pokracovat?")
        if odp.lower() == "ne":
            asses_score(body)
            break
        karta = randint(2,11)
        body = body + karta
        print("Pocitac otocil kartu a hodnota je {}.".format(karta))


if __name__ == '__main__':
    oko_bere()