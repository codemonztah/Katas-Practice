#Price of drink will be a constant in the program
POD=4
wallet=int(input("How much does Wenbin have in his wallet currently?"))
emptyBottle=0
numberofDrinks=0

def buyDrink(POD,wallet):
     wallet= wallet-POD
     return wallet
       
def exchangeBottle(emptyBottle):
    if emptyBottle%2==0:
        return emptyBottle-2,

while wallet>4:
    wallet=buyDrink(POD,wallet)
    numberofDrinks=numberofDrinks+1
    emptyBottle=emptyBottle+1
    if emptyBottle%2==0:
         emptyBottle= emptyBottle-2
         numberofDrinks=numberofDrinks+1


print(numberofDrinks)       

    

    
   







