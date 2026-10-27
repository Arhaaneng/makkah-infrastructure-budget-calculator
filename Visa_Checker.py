
print("--- Makkah Visa Eligibility Checker ---")

answer = int(input("Are you a Muslim? Enter 1 for Yes, 0 for No: "))

if answer == 1:
    print("Access Granted. Welcome to Makkah!")
elif answer == 0:
    print("Access Denied. Entry to the holy city is restricted to Muslims only.")
else:
    print("Invalid input. Please enter 1 or 0.")
  
