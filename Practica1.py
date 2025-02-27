from datetime import datetime

# Fecha de cumple en formato YYYY-MM-DD
birthdate_str = input("Dame tu fecha de cumpleanios (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

# Get the current date
current_date = datetime.now()

# Calculate the age
age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))

print(f"Your age is: {age}")