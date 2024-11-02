# Exercise 2

def AccountAmount():
    AccountBalance = float(input('Enter you account balance'))
    OverDraw = float(input('How many times was the account overdrawn'))

    fee = (AccountBalance / 100 - 5)
    feeTimes = (fee * OverDraw)
    NewBalance = (AccountBalance - feeTimes)

    print(NewBalance)
    print(feeTimes)
    print('Thanks for using this program')
AccountAmount()
    
    
    
# input Account_balance
# input Over_draw

# fee = Account_balance / 100 - 5
# feeTimes = fee * Over_draw
# NewBalance = Acount_balance - feeTimes

# output NewBalance
# output feeTimes
# output Thanks for using this program
