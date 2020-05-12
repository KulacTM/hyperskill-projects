class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.drink_number = None
        self.is_online = True

    def action_choose(self):
        while self.is_online:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            if action == "exit":
                self.is_online = False
            if action == "buy":
                self.action_buy()
            if action == "fill":
                self.action_fill()
            if action == "take":
                self.action_take()
            if action == "remaining":
                self.action_remaining()

    def action_buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.drink_number = input()
        if self.drink_number == "1":
            if self.water < 250:
                print("Sorry, not enough water")
            elif self.coffee_beans < 16:
                print("Sorry, not enough coffee beans")
            elif self.cups < 1:
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.cups -= 1
        if self.drink_number == "2":
            if self.water < 350:
                print("Sorry, not enough water")
            elif self.milk < 75:
                print("Sorry, not enough milk")
            elif self.coffee_beans < 20:
                print("Sorry, not enough coffee beans")
            elif self.cups < 1:
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.cups -= 1
        if self.drink_number == "3":
            if self.water < 200:
                print("Sorry, not enough water")
            elif self.milk < 100:
                print("Sorry, not enough milk")
            elif self.coffee_beans < 12:
                print("Sorry, not enough coffee beans")
            elif self.cups < 1:
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.cups -= 1
        if self.drink_number == "back":
            self.action_choose()
        print("")
        self.action_choose()

    def action_fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())
        print()
        self.action_choose()

    def action_take(self):
        print("I gave you $" + str(self.money))
        self.money = 0
        print()
        self.action_choose()

    def action_remaining(self):
        print()
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee_beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print("$" + str(self.money) + " of money")
        print()
        self.action_choose()


CoffeeMachine = CoffeeMachine()
CoffeeMachine.action_choose()
