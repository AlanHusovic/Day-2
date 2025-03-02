print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people are splitting the bill? "))
total_bill = bill + (bill * tip_percentage / 100)
amount_per_person = total_bill / people
print(f"Each person should pay: $ {amount_per_person:.2f}")
