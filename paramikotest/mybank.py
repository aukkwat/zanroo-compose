class MyBank:
    def __init__(self):
        self.money = 0;
        print "This is init"
    def deposit(self,money):
        self.money += money
        print "your money = " + str(self.money)
    def withdraw(self,money):
        self.money += money
        print "your money = "+ str(self.money)

bank = MyBank()


bank.deposit(1000)
bank.withdraw(500)