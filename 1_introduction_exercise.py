name = input("Enter Your Name:")
age = int(input("Enter your age:"))

from datetime import date
current_year = date.today().year
birth_year = current_year - age

print(f"\nHello, {name}! Nice to meet you.")
print(f"You were probably born in {birth_year}.")
