#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total = 0, items=[]):
    self.discount = discount
    self.total  = total
    self.items = items


  def add_item(self, title, price, quantity= 1):class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount      # discount in percent (e.g., 20 for 20%)
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += float(price) * int(quantity)
        self.items.extend([title] * int(quantity))  # add each item name to list

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    self.total += float(price)*int(quantity)

  def apply_discount(self):
    self.total -= self.total- (self.discount/100)

