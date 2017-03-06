

     
# Item Constants
RICE = 0
VEGGIES = 1
MEAT = 2
SAUCE = 3
CREAM = 4
GUACAMOLE = 5
     

## Cost price dictionary (given) 
COST_PRICE = { RICE : 1, VEGGIES : 1, MEAT : 2, \
              SAUCE : 0.25, CREAM : 1, GUACAMOLE : 1}

## Dictionary for Profit Heuristic
PROFIT = { RICE : 0.1, VEGGIES : 0.1, MEAT : 0.2, \
              SAUCE : 0.05, CREAM : 0.2, GUACAMOLE : 0.2}

SALES_TAX = 4.75 # per cent
    

class RiceBowl(object):
    
    def __init__(self, riceType=None, mixedVeggies=False, \
                 meat=None, sauce=None, sourCream=False, \
                 guacamole=False):
        
        self.riceType = riceType;
        self.mixedVeggies = mixedVeggies;
        self.meat = meat;
        self.sauce = sauce;
        self.sourCream = sourCream;
        self.guacamole = guacamole;
        
        self.costPrice = 0
        self.sellingPrice = 0
        self.tax = 0
        self._calc_prices();
    
    def __del__(self):
        pass
    
    
    def _calc_prices(self):
        self.costPrice = COST_PRICE[RICE]
        self.sellingPrice = PROFIT[RICE]
        
        if self.mixedVeggies:
            self.costPrice += COST_PRICE[VEGGIES]
            self.sellingPrice += PROFIT[RICE]
            
        if self.meat:
            self.costPrice += COST_PRICE[MEAT]
            self.sellingPrice += PROFIT[MEAT]
        
        if self.sauce:
            self.costPrice += COST_PRICE[SAUCE]
            self.sellingPrice += PROFIT[SAUCE]
            
        if self.sourCream:
            self.costPrice += COST_PRICE[CREAM]
            self.sellingPrice += PROFIT[CREAM]
            
        if self.guacamole:
            self.costPrice += COST_PRICE[GUACAMOLE]
            self.sellingPrice += PROFIT[GUACAMOLE]
            
        self.sellingPrice += self.costPrice
        self.tax = self.sellingPrice*SALES_TAX / 100
        self.sellingPrice += self.tax
        
        
    def get_profit(self):
        return self.sellingPrice - self.costPrice - self.tax
    
    
    
""" main() """
print ("Welcome! please select the rice bowl of your choice:\n\n")

rice = input("Add white or brown rice:")
veggies = input("Add mixed vegetables or skip (cost = $1, if chosen):")
meat = input("Add a choice of meat - chicken or beef (cost = $2):")
sauce = input("Add a choice of sauce - spicy or sweet (cost = $0.25):")
cream = input("Add sour cream or skip (cost = $1, if chosen):")
guacamole = input("Add guacamole or skip (cost = $1, if chosen):")

if veggies:
    veggies = True
    
if cream:
    cream = True
    
if guacamole:
    guacamole = True
    
bowl1 = RiceBowl(rice, veggies, meat, sauce, cream, guacamole)
print ("Cost Price: ", bowl1.costPrice, "\n")
print ("Selling Price: " , bowl1.sellingPrice , "\n")
print ("Profit: " , bowl1.get_profit() , "\n")
print ("Tax: ", bowl1.tax , "\n")
    
