"""
Author: Colin Morentin
Date: 3/23/2020
Function: Practice gui with textAreas 
"""

from breezypythongui import EasyFrame

class  paymentPlan(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Payment Plan")
        dataPannel = self.addPanel(row = 0, column = 0)
        #creating different pannels for fun
        dataPannel.addLabel("Purchase Price", row = 0, column = 0)
        #label for purchase price
        self.purchasePrice = dataPannel.addFloatField(value = 0.0, row = 0, column = 1, sticky = "NW")
        #collects data
        buttonPannel = self.addPanel(row = 1, column = 0)
        #creating another pannel for fun
        self.compute = buttonPannel.addButton(text = "compute", row = 0, column = 0, command = self.getPaymentPlan)
        #creating a button
        self.outputSpace = self.addTextArea("", row = 2, column = 0,width = 85, height = 20)
        #creating an areatextBox for output
    def getPaymentPlan(self):
        #fill textarea with requested data
        purchasePrice = self.purchasePrice.getNumber()
        # get data from datafield
        result = ""
        #output string

        ANNUAL_RATE = .12
        MONTHLY_RATE = ANNUAL_RATE / 12
        monthlyPayment = .05 * (purchasePrice - (.10 * purchasePrice))
        month = 1
        balance = purchasePrice
        result += ("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
        while balance > 0:
            if monthlyPayment > balance:
                monthlyPayment = balance
                interest = 0
            else:
                interest = balance * MONTHLY_RATE
            principal = monthlyPayment - interest
            remaining = balance - monthlyPayment
            result+= ("\n\n%2d%15.2f%15.2f%17.2f%17.2f%17.2f" % \
                  (month, balance, interest, principal, monthlyPayment, remaining))
            balance = remaining
            month += 1

        self.outputSpace["state"] = "normal"
        #enable manipulation of areaText
        self.outputSpace.setText(result)
        #fill textbox
        self.outputSpace["state"] = "disabled"
        #put in read status
    

      
        
        
def main():
    paymentPlan().mainloop()

if __name__ == "__main__":
    main()
