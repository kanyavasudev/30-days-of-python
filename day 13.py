
class Cafetaria:

    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        self.start()
    
    def start(self):
      self.choice = input("What do you want to buy? espresso / latte / cappuccino : \n")
      if self.choice == 'espresso':
        self.reduced = [200, 150, 24, 2.5] # water, milk, coffee, money
        if self.resource():   
          self.pay_money()
          self.menu()

      elif self.choice == 'latte':
        self.reduced = [200, 150, 30, 3.5]
        if self.resource():
          self.pay_money()
          self.menu()

      elif self.choice == "cappuccino":
        self.reduced = [150, 250, 24, 4.5]
        if self.resource():
          self.pay_money() 
          self.menu()

      elif self.choice == "report":
        print(f"\nThe coffee machine has: ")
        print(f"Water : {self.water} ml")
        print(f"Milk : {self.milk} ml")
        print(f"Coffee : {self.coffee} g")
        print(f"Money : ${self.money} ")
        self.menu()

      elif self.choice == "off":
        return 0

    def menu(self): # returns to the menu 
        print()
        self.start()

    def resource(self): # checks if enough resourse is there to make coffee
        self.not_available = "" 
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee - self.reduced[2] < 0:
            self.not_available = "coffee"
        
        if self.not_available != "": 
            print(f"Sorry, not enough {self.not_available}!")
            return False
        else: # if everything is enough to make the coffee
            print("Please insert the coins : ")
            return True

    def deduct_resource(self):
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee -= self.reduced[2]
        self.money += self.reduced[3]

    def pay_money(self):
      self.q = int(input("Quarters : "))
      self.d = int(input("Dimes : "))
      self.n = int(input("nickles : "))
      self.p = int(input("pennies : "))
      self.t = (self.q*0.25) + (self.d*0.10) + (self.n*0.05) + (self.p*0.01) 
      #quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
      if (self.t == 2.5):
        print("Here is your " + self.choice + " Enjoy! ")
        self.deduct_resource()
      elif (self.t > 2.5):
        self.b = self.t - 2.5
        print("Here is your " + self.choice + " Enjoy! ")
        print("Here is {:.2f} dollars in change".format(self.b))
        self.deduct_resource()
      elif (self.t < 2.5):
        print("Sorry that's not the enough money")

Cafetaria(800, 500, 200, 5)
OUTPUT:
What do you want to buy? espresso / latte / cappuccino : 
report

The coffee machine has: 
Water : 800 ml
Milk : 500 ml
Coffee : 200 g
Money : $5 

What do you want to buy? espresso / latte / cappuccino : 
latte
Please insert the coins : 
Quarters : 15
Dimes : 5
nickles : 17
pennies : 2
Here is your latte Enjoy! 
Here is 2.62 dollars in change

What do you want to buy? espresso / latte / cappuccino : 
espresso
Please insert the coins : 
Quarters : 19
Dimes : 40
nickles : 68
pennies : 23
Here is your espresso Enjoy! 
Here is 9.88 dollars in change

What do you want to buy? espresso / latte / cappuccino : 

