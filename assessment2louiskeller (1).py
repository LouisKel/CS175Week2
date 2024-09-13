# -*- coding: utf-8 -*-
"""Assessment2LouisKeller

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13axjgVeZl2u_Ad-eq6oVS9-LQRFntMUF
"""

#Inputs
COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75
print("Enter commission rate percentage : " + str(COMMISSION_RATE))
print("Enter number of shares purchased : " + str(NUM_SHARES))
print("Enter purchase price per share : " + str(PURCHASE_PRICE))
print("Enter sell price per share : " + str(SELLING_PRICE))


#declaring variables
amountPaidForStock = 0
purchaseCommission = 0
totalPaid = 0
stockSoldFor = 0
sellingCommission = 0
totalReceived = 0
profitOrLoss = 0


#required calculations on the inputs variables
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommission = amountPaidForStock * COMMISSION_RATE
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommission = COMMISSION_RATE * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid


#outputs
print("Amount paid for the stock : $" + str(amountPaidForStock))
print("Commission paid on the purchase : $" + str(purchaseCommission))
print("Amount the stock sold for : %" + str(stockSoldFor))
print("Commission paid on the sale : %" + str(sellingCommission))
print("Profit (or loss if negative) : $" + str(profitOrLoss))