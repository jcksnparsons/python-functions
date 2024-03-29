dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def calc_coins(dollarAmount, **piggyBank):
    for coins in piggyBank.keys():
        cents = dollarAmount * 100
        remainingMoney = 0

        if coins == "quarters":
            piggyBank["quarters"] = int(cents / 25)
            remainingMoney += cents % 25
            
            if remainingMoney != 0:
                piggyBank["dimes"] = int(remainingMoney / 10)
                remainingMoney = remainingMoney % 10
               
                if remainingMoney != 0:
                   piggyBank["nickels"] = int(remainingMoney / 5)
                   remainingMoney = remainingMoney % 5
            
                   if remainingMoney != 0:
                       piggyBank["pennies"] = int(remainingMoney)
        
    print(piggyBank)


calc_coins(dollarAmount, **piggyBank)