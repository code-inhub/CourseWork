class Apparel:
    
    count = 100
    
    def __init__(self,price, item_type):
        
        self.item_type = item_type
        Apparel.count += 1
        if self.item_type == 'Cotton':
            a = 'C'
        else:
            a = 'S'
        self.item_id = a + str(Apparel.count)
        
        self.price = price + (0.05*price)
        
class Cotton(Apparel):
    
    def calculate_price(self, discount):
        discount = float(discount/100)
        self.price = self.price - (discount*self.price)
        self.price = self.price + (0.05*self.price)
        
        return self.item_id, self.price
    
class Silk(Apparel):
    
    def calculate_price(self):
        
        if self.price>10000:
            points = 10
        else:
            points = 3
            
        self.price = self.price + (0.1*self.price)
        
        return  self.item_id,points, self.price
    
Cot = Cotton(1000, 'Cotton')
Sil = Silk(1000, 'Silk')

discount = int(input("Enter discount on cotton (in percentage): "))
print(Cot.calculate_price(discount))
print(Sil.calculate_price())