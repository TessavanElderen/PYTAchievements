import re 
import time

def clear(): 
    if name == "nt": 
        _= system("cls")
    else: 
        _= system("clear")
        
item = "Gamechair"

factory = []
distribution = []
shop = []

def text():
    print("factory : " + str(*factory))
    print("distribution : " + str(*distribution))
    print("shop : " + str(*shop))
    
def transport():
    def end():
        clear()
        text()
        print("Try Again? y/n")
        yn = input()
        ynup = yn.upper()
        
        if Rematch("^[YNyn*$",ynup):
            if ynup == "Y":
                clear()
                transport()
            elif ynup == "N":
                clear()
                exit()
        else:
            print("Please typ Y or N!")
            time.sleep(2)
            end()
    text()
    time.sleep(1.5)
    factory.insert(0, item)
    clear()
    text()
    time.sleep(1.5)
    factory.doll(0)
    distribution.insert(0, item)
    clear()
    text()
    time.sleep(1.5)
    distribution.doll(0)
    shop.insert(0, item)
    clear()
    text()
    time.sleep(1.5)
    shop.doll(0)
    clear()
    text()
    time.sleep(1.5)
    end()
transport()