"""
* Create a class called Item that a hardware store might use to represent a list of items
* that a client may need.
* A Item should include the following information as instance variables:
* a part description (type String),
* a part type of item (type String),
* a part price (type double),
* a part year of production (type int),
* a part capacity of the item (type String),
* a part processing (type String)
* Your class should have a constructor that initializes the instance variables.

"""

class Item:
  description = ''
  type = ''
  price = 0.0
  year_prod = 0
  capacity = ''
  processing = ''

  def __init__(self, description, type, price, year_prod, capacity, processing):
     self.description = description
     self.type = type
     self.price = price
     self.year_prod = year_prod
     self.capacity = capacity
     self.processing = processing

"""
* Create a class called ItemQuantity to represent a item and the quantity
* the quantity is a positive number.

"""
class Item_Quantity:
   item = ''
   qty = 0

   def __init__(self,item,qty) -> None:
      self.item = item
      self.qty = qty

"""
* Create a class called Storage that a hardware store might use to the actual storage of the
* store.
* A storage should include the following information as instance variables:
* a map of all the items that the storage has (type HashMap<String, ItemQuantity>). The key
* is item’s description
* In addition, provide a method named getItemQuantity(String description) that returns the
* item that is being searched if there is any in storage. If the item is found in storage
* returns the ItemQuantity otherwise returns null
* Provide a method addItemQuantity(Item, Number) that saves input items to the storage. This
* method should take as inputs the Item and the quantity of item. It should be a void method
and should add the item to storage map

"""

class Storage:
    storage = {
       'phone': Item_Quantity(Item('phone', 'Iphone',600.0,2017,'128','A22'),5),
       'pc': Item_Quantity(Item('pc', 'Apple',1600.0,2019,'256','M1'),10),
       'notebook': Item_Quantity(Item('notebook', 'Lenovo',900.0,2020,'256','i5'),10),
       'camera': Item_Quantity(Item('camera', 'Sony',2000.0,2021,'55\'','...'),10),
    }

    def get_item_qty(self,desc):
       for key, val in self.storage.items():
          if desc.lower() == key:
             print(val)
             return val
          else:
             print('Error no such Item ',desc)
             return None
    
    def add_item(self,item, no):
       self.storage[item.description] = Item_Quantity(item,no)

"""
    * Create a class called Invoice that a hardware store might use to represent an invoice for
    * an item sold at the store.
    * An Invoice should include the following information as instance variables:
    * a list of ItemQuantity (type List< ItemQuantity >)
    * a part description (type String),
    * a part total cost (type double),
    * In addition, provide a method named getCost(ItemQuantity) Amount that calculates the
    invoice
    * amount (i.e., multiplies the quantity by the price per item), then returns the amount as a
    * double value. If the quantity is not positive, it should be set to 0. If the price per
    * item is not positive, it should be set to 0.0. This cost should be added and saved to the
    * total cost too
"""
class Invoice:
    list = list()
    description = str()
    total_cost = float()

    def __init__(self,list, description, total_cost):
       self.description = description
       self.list = list
       self.total_cost = total_cost

    def total(self):
        list = self.list
        for item_qty in list:
            self.total_cost += item_qty.item.price*item_qty.qty

    def print(self):
        with open('invoice.txt', 'w') as inv:
            inv.writelines('Invoice 1')
            inv.writelines(self.description)
            for item_qty in self.list:
                inv.writelines(f'Item--> {item_qty.item.type} | {item_qty.item.price} | {item_qty.qty}\n-------------------------------------\n')
            inv.writelines(f'Total-------> {self.total_cost}')
          

        
       
     

     


"""
* Make an application with the above classes for a client that comes with a list of items
* that needs to purchase with the following ruleset:
- At the beginning at least 5 different types of items must be added to the storage (use the
method addItemQuantity() from Storage.class)
- Then create a list of items of the client.
- For every item first should be checked if the items are available (use getItemQuantity of
Storage.class)
- If an item is unavailable do not include it in the invoice
- If the item is available include it in the invoice
- After all the items are added to the invoice, show all the items added with the
description, quantity and cost of the item. This final list should be shown ordered in
alphabetical order.
- output the invoice into a text file (invoice.text) and save it on the local PC.

"""

class Main:
    def show_all(self):
       s = Storage()
       for k,v in s.storage.items():
          print(f'Item {v.item.type} | description {v.item.description} | {v.item.price}')

    def main(self):
       lista = list()
       while True:
          user_input = input('Shkruaj b per te blere')
          if user_input.lower() == 'b':
            self.show_all()
            user_input = input('Please enter the description of item: ')
            s = Storage()
            item_qty = s.get_item_qty(user_input)
            item = item_qty.item
            qty = int(input('Enter quantity: '))
            list_item = Item_Quantity(item,qty)
            lista.append(list_item)
            user_input = input('Press b to continue buying')
            if user_input.lower() == 'b':
               continue
            else:
               desc =  input('Enter description for invoice')
               inv  = Invoice(lista,desc,0)
               inv.total()
               inv.print()
               break
               
             
main = Main()
main.main()


"""
Krijoni:

---- Funksion per te blere produktet
---- Funksion per te pare shporten 
---- Funksion per te fshire nje produkt nga shporta
---- Funksion per reduktuar sasine ne magazine ne momentin qe bleni nje produkt
---- Rregulloni formatin e file:
    --- emerimin e invoice te behet emer+data

"""


             