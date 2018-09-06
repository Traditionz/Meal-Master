# Ziwei Hou CS-171 B, ID: zh367
print("Student Loan Calculator")
# Principle: The amount of money loaned.
P = float(input("Enter in the amount of loan in dollars with no commas or characters:\n"))
# The number of years the loan is for.
y = int(input("Enter the number of years the loan will be for:\n"))
# The times per year interest is compunded. t = 12
t = 12
# subsidized Float interest rate
i = 0.034
# Loan fee rate
f = 0.01051
# Monthly payment
M = (P * i) / (t * (1 - ((1 + (i / t)) ** (-1 * y * t))))

print("___________________________________________________________")
#Subsidized Loan
print("Subsidized Federal Direct Loan")
print("Principle: $", int(P))
print("Interest Rate", round(i*100,2),"%")
print("Years:", y)
print("Monthly Payment: $", round(M,2))
Balance = M * t * y
print("Total Paid on loan: $", round(Balance,2))
Interest_paid = Balance - P
print("Total Interest Paid: $", round(Interest_paid,2))
Fee = P * f
print("Additional Fees Paid: $",round(Fee,2))
total_over = Fee + Interest_paid
print("Total Costs Over Principle: $",round(total_over,2))
print("___________________________________________________________")
#Unsubsidized Loan, 1 means Unsubsidized Loan variables
print("Unsubsidized Federal Direct Loan")
i1 = 0.068
P1 = P * (1 + (i1 * 4.25))
print("Subsidized Federal Direct Loan")
print("Principle: $", int(P))
print("Interest Rate", round(i1*100,2),"%")
print("Years:", y)
M1 = (P1 * i1) / (t * (1 - ((1 + (i1 / t)) ** (-1 * y * t))))
print("Monthly Payment: $",round(M1,2))
Balance1 = M1 * t * y
print("Total Paid on loan: $", round(Balance1,2))
Interest_paid1 = Balance1 - P
print("Total Interest Paid: $", round(Interest_paid1,2))
print("Additional Fees Paid: $",round(Fee,2))
total_over1 = Fee + Interest_paid1
print("Total Costs Over Principle: $",round(total_over1,2))
print("___________________________________________________________")
#Federal Plus Loan, 2 means Plus Loan variables
print("Federal Plus Loan")
i2 = 0.079
f2 = 0.04204
P2 = P * (1 + (i2 * 4.25))
print("Principle: $", int(P))
print("Interest Rate", i2*100,"%")
print("Years:", y)
M2 = (P2 * i2) / (t * (1 - ((1 + (i2 / t)) ** (-1 * y * t))))
print("Monthly Payment: $",round(M2,2))
Balance2 = M2 * t * y
print("Total Paid on loan: $", round(Balance2,2))
Interest_paid2 = Balance2 - P
print("Total Interest Paid: $", round(Interest_paid2,2))
Fee2 = P * f2
print("Additional Fees Paid: $",round(Fee2,2))
total_over2 = Fee2 + Interest_paid2
print("Total Costs Over Principle: $",round(total_over2,2))
