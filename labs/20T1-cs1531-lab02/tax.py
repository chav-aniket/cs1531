import locale
locale.setlocale(locale.LC_ALL, "")

income = float(input("Enter your income: "))
tax = 0
if income > 180000:
    tax = 54232+0.45*(income-180000)
elif income>87000:
    tax = 19822+0.37*(income-87000)
elif income>37000:
    tax = 3572+0.325*(income-37000)
elif income>18200:
    tax = 0.19*(income-18200)
else:
    pass

tax = locale.currency(round(tax, 2), grouping=True)

print(f"The estimated tax on your income is {tax}")