IPHONE_128_PRICE = 300
IPHONE_256_PRICE = 350
SAMSUNG_128_PRICE = 220
SAMSUNG_256_PRICE = 270
SONY_128_PRICE = 190
SONY_256_PRICE = 210

orders = []

class Phone_Order:
  def __init__(self,phone,capacity,price):
    self.phone = phone
    self.capacity = capacity
    self.price = price

def get_phone_order():
  phone = int(input("select phone please \n1. Iphone\n2. Samsung\n3.Sony\nSelection:"))
  capacity = int(input("select phone capacity: \n1. 128\n2. 256\nSelection:"))
  if phone == 1 and capacity == 1:
    orders.append(Phone_Order("IPhone",128,IPHONE_128_PRICE))
  elif phone == 1 and capacity == 2:
    orders.append(Phone_Order("IPhone",256,IPHONE_256_PRICE))
  elif phone == 2 and capacity == 1:
    orders.append(Phone_Order("Samsung",128,SAMSUNG_128_PRICE))
  elif phone == 2 and capacity == 2:
    orders.append(Phone_Order("Samsung",128,SAMSUNG_256_PRICE))
  elif phone == 3 and capacity == 1:
    orders.append(Phone_Order("Sony",128,SONY_128_PRICE))
  elif phone == 3 and capacity == 2:
    orders.append(Phone_Order("Sony",256,SONY_256_PRICE)) 
  else:
    print("Not a correct order")

def print_order():
  total_order = 0
  for order in orders:
    print("type: ",order.phone,order.capacity,":",order.price)
    total_order = total_order + order.price
  print("Total price is:",total_order)

cont = 1
while cont != 0:
  get_phone_order()
  cont = int(input("Want to add an phone order:\n0. No\n1. Yes\nSelection:"))

print_order()

