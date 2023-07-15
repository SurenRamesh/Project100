class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def CashWithdrawal(self):
        print("You have withdrawed 500000 rupee.")
        
    def BalanceEnquiry(self):
        print("Your total balance is 1 rupee.")

new_user = Atm(123, 2039)

new_user.CashWithdrawal()
new_user.BalanceEnquiry()

