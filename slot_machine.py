import numpy

def slot_machine():

    class slots:
        symbols = ["A", "B", "C", "D", "E", "F", "G"]
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
        while (bet > credits):
            print("You don't have enough credits for that bet.")
            bet = int(input("Please, insert a valid number of credits: "))

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
            if (check != "y"):
                continue_playing = False

slot_machine()