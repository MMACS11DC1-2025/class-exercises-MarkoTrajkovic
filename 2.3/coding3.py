"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""
burger_cost = 0
fries_cost = 0

print("Would you like a burger for $5?")
burger = input().lower()
print("Would you like fries for $3?")
fries = input().lower()

if burger == "yes":
    burger_cost = 5
elif burger == "no":
    burger_cost = 0

if fries == "yes":
    fries_cost = 3
elif fries == "no":
    fries_cost = 0

total_cost = (burger_cost + fries_cost) * 1.14

print("Your total is: " + str(total_cost))