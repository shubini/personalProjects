#this function is designed to take in a number of years, a number of years and either a lump sum or regular amount and output the final total amount and money gaved from savings

def menu():
    typeSet = False
    savingsRate = float(input("What is the estimated annual interest rate / annual returns of the savings account or investment account you would like to compute?\n"))
    years = int(input("How many years would you like to invest for?\n"))
    while typeSet == False:
        paymentType = (input("Are you going to save via lump sum or via regular payments? Type 'Lump' for lump sum, and 'Regular' for regular payments\n")).lower()
        if paymentType == "lump":
            lumpSum = float(input("How much money are you putting into the savings account (in £)?\n"))
            lumpSavings(savingsRate, years, lumpSum)
            typeSet = True
        elif paymentType =="regular":
            regularSum = float(input("How much money are you putting into the savings account with each payment?\n"))
            regularInterval = float (input("How often would you pay into the account (in years)?\n"))
            regularSavings(savingsRate, years, regularSum, regularInterval)
            typeSet = True
        else:
            print("Didn't quite get that, please type 'Lump' for lump sum, and 'Regular' for regular payments\n")

def lumpSavings(savingsRate, years, lumpSum):
    y2yRatio = float(1 + savingsRate/100)
    endAmount =  lumpSum * (y2yRatio ** years)
    earnings = endAmount - lumpSum
    print("Investing £", str(lumpSum), " for ", str(years), " years at rate of ", str(savingsRate), "% would leave you with £", str(endAmount), " netting you an extra £", str(earnings))

def regularSavings(savingsRate, years, regularSum, regularInterval):
    y2yRatio = float(1 + savingsRate/100)
    runningTotal = 0
    for x in range (0, years):
        if x % regularInterval == 0:
            runningTotal += regularSum
        runningTotal *= y2yRatio
    costs = regularSum*(years/regularInterval)
    print(str(costs))
    earnings = runningTotal - costs
    print("Investing £", str(regularSum), "every ", str(regularInterval), " years for ", str(years), " years at rate of ", str(savingsRate), "% would leave you with £", str(runningTotal), " netting you an extra £", str(earnings))
