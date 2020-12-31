"""
File: taxformwithgui.py
Project 8.6
A GUI-based tax calculator.

Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and tax rates of
20% for Single
15% for Married
10% for Divorced
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")

        # Label and field for the income
        # (self.incomeField)
        self.addLabel(text = "Income", row = 0, column = 0)
        self.incomeField  = self.addFloatField(value = 0.0, row = 0, column = 1)

        # Label and field for the number of dependents
        self.addLabel(text = "Number of dependents", row = 1, column = 0)
        self.dependentField = self.addIntegerField(value = 0, row = 1, column = 1)
        # (self.depField)

        # Radio buttons for filing status
        self.statusGroup = self.addRadiobuttonGroup(row = 3, column = 0, columnspan = 3, orient = "horizonal")
        defaultRB = self.statusGroup.addRadiobutton(text = "Single")
        self.statusGroup.setSelectedButton(defaultRB)
        self.statusGroup.addRadiobutton(text = "Married")
        self.statusGroup.addRadiobutton(text = "Divorced")
        # Button group (self.statusGroup)
        # Option for single (self.single)
        # Option for married (self.married)
        # Option for divorced (self.divorced)
 
        # The compute button
        self.addButton(text = "Compute", row = 4, column = 0, command = self.computeTax)

        # Label and field for the tax
        self.addLabel("Tax", row = 5, column = 0)
        self.taxField = self.addFloatField(value = 0.0, row = 5, column = 1, precision = 2, state = "readonly")

    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field (taxField)."""
        taxIndex = 0
        status = self.statusGroup.getSelectedButton()["text"]
        if status == ("Single"):
            taxIndex = .20
        elif status == ("Married"):
            taxIndex = .15
        else:
            taxIndex = .10
        income = self.incomeField.getNumber()

        dependents = self.dependentField.getNumber()
        
        taxes = (income - 10000 - dependents * 3000 ) * taxIndex
        if taxes < 0:
            taxes = 0

        self.taxField.setNumber(taxes)
        
        
def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()
