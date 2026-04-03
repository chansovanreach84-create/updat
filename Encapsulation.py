class DigitalWallet :
    def __init__(self) :
        self.__balance = float(input("Please Input Your Balance :"))
        self.__pin_code = "reach10steav_kheat"
        
    def get__balance(self) :
        return self.__balance

    
    def desposit(self, addition , PIN) :
            if PIN == self.__pin_code :
                self.__balance += addition
                return f"Your Balance after desposit : {self.__balance}"
            else :
                return "Invalid Account!!!!"
    def withdraw(self, subsraction, PIN) :
        if PIN == self.__pin_code :
            if subsraction > 0 and subsraction <=self.__balance :
                self.__balance -= subsraction 
                return f"Your balance after withdrawal : {self.__balance}"
            else :
                return "Your banlance is not enough!!"
        else :
            return "Invalid Account !!!"
my_digitalwallet = DigitalWallet()
PIN = input("Input Your code : ")
print(my_digitalwallet.desposit(100,PIN))
    
print(my_digitalwallet.withdraw(600,PIN))
    

    