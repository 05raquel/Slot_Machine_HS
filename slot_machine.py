import numpy

def slot_machine():

    class slots:
        symbols = ["#", "@", "&", "0", "£", "+", "*"]
        symbol_1 = "A"
        symbol_2 = "A"
        symbol_3 = "A"
        def __init__(self):
            self.symbol_1 = self.roll()
            self.symbol_2 = self.roll()
            self.symbol_3 = self.roll()
        def roll(self):
            self.symbol_1 = numpy.random.choice(self.symbols, p=[50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156])
            self.symbol_2 = numpy.random.choice(self.symbols, p=[50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156])
            self.symbol_3 = numpy.random.choice(self.symbols, p=[50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156])

    our_slots = slots()
    credits = int(input("Deposit your credits: "))
    continue_playing = True
    if credits == 0:
        continue_playing = False

    while continue_playing == True:

        bet = int(input("How many credits do you wanna bet? "))
        while (bet > credits or bet <= 0):
            if (bet <= 0):
                bet = int(input("Really? Try again: "))
            else:
                w=["Are you stupid? You dont't have enought credits for that bet.", "Please, insert a valid number of credits.", "You're to poor for that bet.", "Are you dumb? Insert a valid number of credits!"]
                s = numpy.random.choice(w)
                print(s)
                bet = int(input("Try again: "))

        our_slots.roll()
        print("\n --------- ")
        print(f"| {our_slots.symbol_1}  {our_slots.symbol_2}  {our_slots.symbol_3} |")
        print(" --------- ")

        if our_slots.symbol_1 == our_slots.symbol_2 and our_slots.symbol_1 == our_slots.symbol_3:
            print("***JACKPOT***")
            points = [5, 10, 20, 70, 200, 1000, 100000]
            i = 0
            found = False
            while i < 7 and not found:
                if our_slots.symbol_1 == our_slots.symbols[i]:
                    credits += bet*points[i]
                    found = True
                i += 1
        else:
            credits -= bet

        print(f"\nYou have {credits} credits left")

        if credits == 0:
            print("GAME OVER")
            continue_playing = False
        else:
            check = input("Do you wanna keep playing? (y/n)) ")
            if (check == "n"):
                continue_playing = False
                print(f"\nYou ended up with {credits} credits. Congrats! (or I'm sorry if you're poor now)")

slot_machine()