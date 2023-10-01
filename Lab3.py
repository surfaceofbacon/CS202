filing_status = float(input('Enter the filing status: '))
constant_taxable_income = float(input('Enter the taxable income: '))
rate = 0
tax = 0
taxable_income = constant_taxable_income
if filing_status == 0:
    tax_bracket = {8350: 0.1, 33950: 0.15, 82250: 0.25, 171550: 0.28, 372950: 0.33, 372952: 0.35}
elif filing_status == 1:
    tax_bracket = {16700: 0.1, 67900: 0.15, 137050: 0.25, 208850: 0.28, 372950: 0.33, 372951: 0.35}
elif filing_status == 2:
    tax_bracket = {8350: 0.1, 33950: 0.15, 68525: 0.25, 104425: 0.28, 186475: 0.33, 186476: 0.35}
elif filing_status == 3:
    tax_bracket = {11950: 0.1, 45500: 0.15, 117450: 0.25, 190200: 0.28, 372950: 0.33, 372951: 0.35}
else:
    tax_bracket = {}

for key in tax_bracket:
     if constant_taxable_income >= key and taxable_income > 0:
         if taxable_income - key >= 0:


            taxable_income -= key
            tax += key * tax_bracket[key]
         else:
            tax += taxable_income*tax_bracket[key]


print('Tax is', tax)