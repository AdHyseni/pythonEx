class Items():
    def __init__(self,emri, desc, price, viti_prodh) -> None:
        self.emri = emri
        self.desc = desc
        self.price = price
        self.viti_prodh = viti_prodh


class Item_qty():
    def __init__(self,item,qty) -> None:
        self.item = item
        self.qty = qty

    
class Bill():
    def __init__(self,item_qty, date,total):
        self.item_qty = item_qty
        self.date = date
        self.total = total
    
class Storage():
    items_storage = {
        1: Item_qty(Items(emri='HP',desc='Laptop',price=300,viti_prodh=2010),qty=10),
        2: Item_qty(Items(emri='Xiaomi',desc='Monitor',price=200,viti_prodh=2020),qty=10),
        3: Item_qty(Items(emri='Apple',desc='Iphone',price=1300,viti_prodh=2021),qty=10),
        4: Item_qty(Items(emri='Boose',desc='Kufje',price=100,viti_prodh=2010),qty=10),
        5: Item_qty(Items(emri='Panasonic',desc='TV',price=330,viti_prodh=2010),qty=10),
        6: Item_qty(Items(emri='Sony',desc='Aparat Fotografik',price=3000,viti_prodh=2021),qty=10)
            }
        
    def show_items(self):
        for key,values in self.items_storage.items():
            print(f'Emri {values.item.emri} ,Cmimi {values.item.price}, viti i prodhimit: {values.item.viti_prodh}, sasia {values.qty}') # Printoni dhe te dhenat e tjera
    
    
    def search_item(self):
        input_name = input("Vendos emrin e produktit qe doni te kontrolloni: ")
        counter = 0
        for key,value in self.items_storage.items():
            counter +=1
            if input_name == value.item.emri:
                print(f'Produkti {value.item.emri} ndodhet ne dyqan dhe ka {value.qty} njesi te mbetura')
                break
            elif counter >= len(self.items_storage.items()): 
                print('Produkti nuk gjendet ne dyqanin tone')
    
    def add_item(self, e, d, p, v,q):
        last_key = list(self.items_storage)[-1]
        new_key = last_key +1
        print(new_key)
        self.items_storage[new_key] = Item_qty(Items(e, d,p,v),q)

    def buy_item(self,name,qty_def):
        counter = 0
        for k,v in self.items_storage.items():
            counter += 1
            if name == v.item.emri:
                if qty_def <= v.qty:
                    new_qty = v.qty - qty_def
                    self.items_storage.update({k:Item_qty(Items(v.item.emri,v.item.desc,v.item.price,v.item.viti_prodh),new_qty)})
                    return Item_qty(Items(name,v.item.desc,v.item.price,v.item.viti_prodh),qty_def)
                else:
                    print('Sasia eshte me e madhe se sasia e ruajtur ne magazine')
                    return 0
            elif counter >= len(self.items_storage.items()):
                print('Produkti nuk ekziston')
                return 0


        
# storage = Storag()
# y = storage.buy_item('HP',2) # vlera e funksionit eshte nje objekt

# print('Objekti ',y)
# storage.search_item()

from datetime import date

class Kasa():
    shporta = {}

    def buy(self):
        storage = Storage() #i referohet klases Storage, nga ktu mund te therrasim cdo sjellje te Storage
        a = True # Kontrollon ciklin
        key = 1 # Eshte celsi i fjalorit(shporta)
        
        while a: 
            prod_name = input('Shkruaj emrin e produktit ') #Kerkojme emrin e item
            prod_qty = input('Shkruaj sasine ') #Sasine qe duam te blem
            produkti = storage.buy_item(prod_name,int(prod_qty)) #Ne momentin qe therrasim buy_item nga storage ne marrim nje objekt me te dhenat e item dhe sasin
            if produkti == 0:
                print("Nuk mund te bej blerjen")
            else:
                totali_per_produkt = int(prod_qty)*produkti.item.price
                self.shporta[key] = Bill(produkti,date.today(),totali_per_produkt)
                user_input = input('Shkruaj po per te vazhduar ose cdo gje tjt per te dale ')
                if user_input == 'po':
                    a = True
                    key +=1 #inkremento celsin
                else:
                    a = False
                    with open(f'fatura-{date.today()}.txt','w') as f:
                        totali = 0
                        for k,v in self.shporta.items():
                            totali += v.total
                        for k,v in self.shporta.items():
                            f.writelines(f'{k}--Emri i produktit: {v.item_qty.item.emri}---Pershkrimi: {v.item_qty.item.desc}---Totali: {v.total}\n')
                        f.writelines(f'--------------Totali per te paguar eshte: {totali} Eu \n')

    
    
    
    def main(self):
        user_input = input('Shkruaj 1 per te pare produktet\nShkruaj 2 per te kerkuar nje produkt\nShkruaj 3 per te blere nje produkt:\n')
        storage = Storage()
        match user_input:
            case '1':
                storage.show_items()
            case '2':
                storage.search_item()
            case '3':
                self.buy()
            case _:
                print('Faleminderit qe blete ne dyqanin tone')


kasa = Kasa()
kasa.main()