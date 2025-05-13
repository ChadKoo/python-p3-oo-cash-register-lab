#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount      # discount in percent (e.g., 20 for 20%)
        self.total = 0
        self.items = []
        self.last_transaction = 0
       


    def add_item(self, title, price, quantity=1):
      amount = float(price) * int(quantity)
      self.total += amount
      self.last_transaction = amount  # Save last transaction
      self.items.extend([title] * int(quantity))


    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction

 

