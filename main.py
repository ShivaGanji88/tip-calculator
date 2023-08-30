#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Welcome to the tip calculator!")

bill_amount = float(input("what was the total bill?  "))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))
adding_tip = tip_percentage / 100

split_bill = int(input("how many members bill split with? "))

tip_add = bill_amount * adding_tip
total_bill = bill_amount + tip_percentage
people_divide = total_bill / split_bill
rounding_num = round(people_divide, 2)


print(f"Each person should pay {rounding_num}")